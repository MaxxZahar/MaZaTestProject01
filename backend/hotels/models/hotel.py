from django.db import models
from .feature import Feature
from ..settings import HOTEL_TYPES


class Hotel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    type = models.CharField(max_length=25, choices=HOTEL_TYPES, verbose_name='Тип жилья')
    price = models.IntegerField(verbose_name='Цена')
    stars = models.IntegerField(verbose_name='Звёзды')
    rating = models.FloatField(verbose_name='Рейтинг')
    img = models.ImageField(blank=True, null=True, verbose_name='Фотография')
    alt = models.CharField(max_length=255, blank=True, null=True, verbose_name='Текст к фотографии')
    features = models.ManyToManyField(Feature, related_name='hotel_features', verbose_name='Инфраструктура')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'

