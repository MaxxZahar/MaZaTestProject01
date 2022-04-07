from django.db import models


class Reason(models.Model):
    title = models.CharField(max_length=50, verbose_name='Причина')
    number = models.IntegerField(verbose_name='Номер')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Причина'
        verbose_name_plural = 'Причины'
        ordering = ("number",)

