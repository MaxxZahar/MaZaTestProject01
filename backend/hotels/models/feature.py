from django.db import models


class Feature(models.Model):
    type = models.CharField(max_length=50, verbose_name='Тип')
    value = models.FloatField(blank=True, null=True, verbose_name='Значение')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    html_form_name = models.CharField(max_length=25, blank=True, null=True, verbose_name='Имя для HTML формы')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Инфраструктура'
        verbose_name_plural = 'Инфраструктура'