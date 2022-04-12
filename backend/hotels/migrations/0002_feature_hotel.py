# Generated by Django 3.1 on 2022-04-12 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, verbose_name='Тип')),
                ('value', models.FloatField(blank=True, null=True, verbose_name='Значение')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Инфраструктура',
                'verbose_name_plural': 'Инфраструктура',
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('type', models.CharField(choices=[('Гостиница', 'Гостиница'), ('Мотель', 'Мотель'), ('Апартаменты', 'Апартаменты')], max_length=25, verbose_name='Тип жилья')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('stars', models.IntegerField(verbose_name='Звёзды')),
                ('rating', models.FloatField(verbose_name='Рейтинг')),
                ('features', models.ManyToManyField(related_name='hotel_features', to='hotels.Feature', verbose_name='Инфраструктура')),
            ],
            options={
                'verbose_name': 'Отель',
                'verbose_name_plural': 'Отели',
            },
        ),
    ]