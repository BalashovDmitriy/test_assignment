# Generated by Django 5.0.1 on 2024-01-18 05:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('model', models.CharField(max_length=100, verbose_name='Модель')),
                ('release_date', models.DateField(verbose_name='Дата выхода продукта на рынок')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('country', models.CharField(max_length=100, verbose_name='Страна')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('street', models.CharField(max_length=100, verbose_name='Улица')),
                ('house', models.CharField(max_length=100, verbose_name='Дом')),
                ('debt', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Задолженность')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='the_net.product')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='the_net.seller', verbose_name='Поставщик')),
            ],
        ),
    ]