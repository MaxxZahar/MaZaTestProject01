from django.db import models
from .feature import Feature


class Hotel(models.Model):
    HOTEL_TYPES = (
        ('Гостиница', 'Гостиница'),
        ('Мотель', 'Мотель'),
        ('Апартаменты', 'Апартаменты')
    )
    name = models.CharField(max_length=255, verbose_name='Название')
    type = models.CharField(max_length=25, choices=HOTEL_TYPES, verbose_name='Тип жилья')
    price = models.FloatField(verbose_name='Цена')
    stars = models.IntegerField(verbose_name='Звёзды')
    rating = models.FloatField(verbose_name='Рейтинг')
    features = models.ManyToManyField(Feature, related_name='hotel_features', verbose_name='Инфраструктура')

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'

