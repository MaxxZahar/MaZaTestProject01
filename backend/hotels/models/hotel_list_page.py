from django.db import models
from garpix_page.models import BaseListPage


class HotelListPage(BaseListPage):
    paginate_by = 3
    template = 'pages/hotel_list.html'

    class Meta:
        verbose_name = "Список отелей"
        verbose_name_plural = "Списки отелей"
        ordering = ('-created_at',)
