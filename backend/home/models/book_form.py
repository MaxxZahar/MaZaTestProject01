from django.db import models
from hotels.models import Hotel
from django.utils import timezone


class BookFormModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.EmailField(verbose_name='Адрес электронной почты')
    arrival_date = models.DateField(verbose_name='День прибытия')
    departure_date = models.DateField(verbose_name='День отъезда')
    number_of_adults = models.IntegerField(verbose_name='Число взрослых')
    number_of_children = models.IntegerField(verbose_name='Число детей')
    hotel = models.ForeignKey(Hotel, on_delete=models.RESTRICT, related_name='book_hotel', verbose_name='Отель')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Время бронирования')

    class Meta:
        verbose_name = 'Модель для формы бронирования'
        verbose_name_plural = 'Модели для формы бронирования'
        ordering = ('-created_at', )
