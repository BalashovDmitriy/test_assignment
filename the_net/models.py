from django.db import models


class Seller(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    contacts = models.ForeignKey('Contacts', on_delete=models.CASCADE, verbose_name='Контакты')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Продукт')
    provider = models.ForeignKey('Seller', on_delete=models.CASCADE, verbose_name='Поставщик')
    debt = models.PositiveIntegerField(default=0, verbose_name='Задолженность')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')


class Contacts(models.Model):
    email = models.EmailField(max_length=100, verbose_name='Email')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house = models.CharField(max_length=100, verbose_name='Дом')

    def __str__(self):
        return f'{self.email} - {self.country} - {self.city} - {self.street} - {self.house}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    model = models.CharField(max_length=100, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода продукта на рынок')

    def __str__(self):
        return f'{self.title} - {self.model} - {self.release_date}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
