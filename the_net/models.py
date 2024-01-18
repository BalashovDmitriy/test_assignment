from django.db import models

from users.models import NULLABLE


class Seller(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    email = models.EmailField(max_length=100, verbose_name='Email')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house = models.CharField(max_length=100, verbose_name='Дом')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    supplier = models.ForeignKey('Seller', on_delete=models.CASCADE, verbose_name='Поставщик', **NULLABLE)
    debt = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Задолженность')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')

    def __str__(self):
        return f'{self.title} - {self.country} - {self.city}'

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    model = models.CharField(max_length=100, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода продукта на рынок')

    def __str__(self):
        return f'{self.title} - {self.model} - {self.release_date}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
