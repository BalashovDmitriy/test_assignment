from rest_framework.test import APITestCase

from the_net.models import Seller, Product
from users.models import User


class SellerAndProductTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='example@example.com', is_active=True)
        self.user.set_password('password123')
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.seller_factory = Seller.objects.create(
            title='Factory',
            supplier=None,
            email='zavod@example.com',
            country='Russia',
            city='Moscow',
            street='Zavodskaya',
            house='1B/2',
            debt=12500000,
        )
        self.seller_retailer = Seller.objects.create(
            title='Retailer',
            supplier=self.seller_factory,
            email='retailer@example.com',
            country='Belarus',
            city='Minsk',
            street='Agapovskaya',
            house='29',
            debt=500000,
        )
        self.seller_individual = Seller.objects.create(
            title='Individual',
            supplier=self.seller_retailer,
            email='individual@example.com',
            country='Russia',
            city='Chelyabinsk',
            street='Enthusiastov',
            house='3',
            debt=34600,
        )
        self.product = Product.objects.create(
            title='Notebook',
            model='SM-500 Ultra',
            release_date='2020-01-01',
            seller=self.seller_individual,
        )

    def test_get_sellers(self):
        response = self.client.get('/api/suppliers/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                         [
                             {
                                 'title': self.seller_factory.title,
                                 'supplier': self.seller_factory.supplier,
                                 'email': self.seller_factory.email,
                                 'country': self.seller_factory.country,
                                 'city': self.seller_factory.city,
                                 'street': self.seller_factory.street,
                                 'house': self.seller_factory.house,
                                 'debt': self.seller_factory.debt,
                                 'products': [],
                             },
                             {
                                 'title': self.seller_retailer.title,
                                 'supplier': self.seller_retailer.supplier_id,
                                 'email': self.seller_retailer.email,
                                 'country': self.seller_retailer.country,
                                 'city': self.seller_retailer.city,
                                 'street': self.seller_retailer.street,
                                 'house': self.seller_retailer.house,
                                 'debt': self.seller_retailer.debt,
                                 'products': [],
                             },
                             {
                                 'title': self.seller_individual.title,
                                 'supplier': self.seller_individual.supplier_id,
                                 'email': self.seller_individual.email,
                                 'country': self.seller_individual.country,
                                 'city': self.seller_individual.city,
                                 'street': self.seller_individual.street,
                                 'house': self.seller_individual.house,
                                 'debt': self.seller_individual.debt,
                                 'products': [
                                     {'title': self.product.title,
                                      'release_date': self.product.release_date,
                                      'model': self.product.model,
                                      'seller': self.product.seller.id,
                                      }
                                 ],
                             },
                         ])

    def test_get_products(self):
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                         [
                             {
                                 'title': self.product.title,
                                 'model': self.product.model,
                                 'release_date': self.product.release_date,
                                 'seller': self.product.seller.id,
                             },
                         ])

    def test_create_seller(self):
        data = {
            'title': 'Test',
            'supplier': self.seller_individual.id,
            'email': 'test@example.com',
            'country': 'Test',
            'city': 'Test',
            'street': 'Test',
            'house': 'Test',
            'debt': 50,
        }
        response = self.client.post('/api/suppliers/', data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Seller.objects.count(), 4)
        self.assertEqual(Seller.objects.get(id=4).level, 2)

    def test_get_product_by_id(self):
        response = self.client.get(f'/api/products/{self.product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                         {
                             'title': self.product.title,
                             'model': self.product.model,
                             'release_date': self.product.release_date,
                             'seller': self.product.seller.id,
                         })

    def test_get_sellers_by_id(self):
        response = self.client.get(f'/api/suppliers/{self.seller_individual.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                         {
                             'title': self.seller_individual.title,
                             'supplier': self.seller_individual.supplier_id,
                             'email': self.seller_individual.email,
                             'country': self.seller_individual.country,
                             'city': self.seller_individual.city,
                             'street': self.seller_individual.street,
                             'house': self.seller_individual.house,
                             'debt': self.seller_individual.debt,
                             'products': [
                                 {'title': self.product.title,
                                  'release_date': self.product.release_date,
                                  'model': self.product.model,
                                  'seller': self.product.seller.id,
                                  }
                             ],
                         })

    def test_update_product(self):
        data = {
            'title': 'Notebook',
            'model': 'SM-500 Ultra',
            'release_date': '2020-01-01',
            'seller': self.seller_individual.id,
        }
        response = self.client.put(f'/api/products/{self.product.id}/', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                         {
                             'title': 'Notebook',
                             'model': 'SM-500 Ultra',
                             'release_date': '2020-01-01',
                             'seller': self.seller_individual.id,
                         })

    def test_delete_product(self):
        response = self.client.delete(f'/api/products/{self.product.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Product.objects.count(), 0)

    def test_update_seller(self):
        data = {
            'title': 'Test',
            'supplier': self.seller_individual.id,
            'email': 'test@example.com',
            'country': 'Test',
            'city': 'Test',
            'street': 'Test',
            'house': 'Test',
            'debt': 50,
        }
        response = self.client.put(f'/api/suppliers/{self.seller_individual.id}/', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'Ошибка': 'Вы не можете изменить поле задолженности'})

    def test_delete_seller(self):
        response = self.client.delete(f'/api/suppliers/{self.seller_individual.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Seller.objects.count(), 2)
