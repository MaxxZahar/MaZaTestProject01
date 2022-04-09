from django.db import models


class SearchFormModel(models.Model):
    arrival_date = models.DateField(verbose_name='Дата прибытия')
    departure_date = models.DateField(verbose_name='Дата отъезда')
    number_of_adults = models.IntegerField(verbose_name='Количество взрослых')
    number_of_children = models.IntegerField(verbose_name='Количество детей')

    class Meta:
        verbose_name = 'Модель для формы поиска'
        verbose_name_plural = 'Модели для формы поиска'
    