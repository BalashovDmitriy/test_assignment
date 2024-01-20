from django.db import models

from users.models import NULLABLE


class Seller(models.Model):
    level = models.PositiveSmallIntegerField(verbose_name='Уровень')
    supplier = models.ForeignKey('Seller', verbose_name='Поставщик', on_delete=models.SET_NULL, **NULLABLE)
    title = models.CharField(max_length=100, verbose_name='Название')
    email = models.EmailField(max_length=100, verbose_name='Email')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house = models.CharField(max_length=100, verbose_name='Дом')
    debt = models.PositiveIntegerField(default=0, verbose_name='Задолженность перед поставщиком')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def save(self, *args, **kwargs):
        if self.supplier is None:
            self.level = 0
        elif self.supplier.supplier is None:
            self.level = 1
        else:
            self.level = 2
        super(Seller, self).save(*args, **kwargs)


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    model = models.CharField(max_length=100, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода продукта на рынок')
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, verbose_name='Поставщик', **NULLABLE,
                               related_name='products')

    def __str__(self):
        return f'{self.title} - {self.seller} - {self.release_date}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
