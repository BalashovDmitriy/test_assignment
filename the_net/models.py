from django.db import models

from users.models import NULLABLE

choices = (
    (0, 'Factory'),
    (1, 'Retail'),
    (2, 'Individual'),
)


class Seller(models.Model):
    level = models.IntegerField(choices=choices, verbose_name='Уровень')
    title = models.CharField(max_length=100, verbose_name='Название')
    email = models.EmailField(max_length=100, verbose_name='Email')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house = models.CharField(max_length=100, verbose_name='Дом')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    model = models.CharField(max_length=100, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода продукта на рынок')
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, verbose_name='Поставщик', **NULLABLE)

    def __str__(self):
        return f'{self.title} - {self.seller} - {self.release_date}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Connector(models.Model):
    supplier = models.ForeignKey(Seller, on_delete=models.SET_NULL, verbose_name='Поставщик', **NULLABLE)
    debt = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Задолженность перед поставщиком')
    products = models.ManyToManyField(Product, verbose_name='Продукты')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.supplier} - {self.debt} - {self.products}'

    class Meta:
        verbose_name = 'Связь'
        verbose_name_plural = 'Связи'
