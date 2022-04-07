from django.db import models
from .reason import Reason


class Recommendation(models.Model):
    title = models.CharField(max_length=35, verbose_name="Область рекоммендации")
    text = models.TextField(verbose_name='Рекоммендация')
    reason = models.ForeignKey(Reason, on_delete=models.CASCADE, related_name='reason_recommendation', verbose_name='Причина',
                               default=1)

    class Meta:
        verbose_name = 'Рекоммендация'
        verbose_name_plural = 'Рекоммендации'
        order_with_respect_to = 'reason'


