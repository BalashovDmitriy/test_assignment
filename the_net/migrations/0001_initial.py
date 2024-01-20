# Generated by Django 5.0.1 on 2024-01-20 15:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField(verbose_name='Уровень')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('country', models.CharField(max_length=100, verbose_name='Страна')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('street', models.CharField(max_length=100, verbose_name='Улица')),
                ('house', models.CharField(max_length=100, verbose_name='Дом')),
                ('debt', models.PositiveIntegerField(default=0, verbose_name='Задолженность перед поставщиком')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='the_net.seller', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('model', models.CharField(max_length=100, verbose_name='Модель')),
                ('release_date', models.DateField(verbose_name='Дата выхода продукта на рынок')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='the_net.seller', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
