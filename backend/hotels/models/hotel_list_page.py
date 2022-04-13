from django.db import models
from garpix_page.models import BaseListPage


class HotelListPage(BaseListPage):
    paginate_by = 25
    template = 'pages/hotel_list.html'

    def get_context(self, request=None, *args, **kwargs):
        from .hotel import Hotel
        from ..serializers import HotelSerializer
        context = super().get_context(request, *args, **kwargs)
        hotels = HotelSerializer(Hotel.objects.all(), many=True).data
        context.update({
            'hotels': hotels
        })
        for hotel in context['hotels']:
            hotel.update({'range': list(range(hotel['stars']))})
        return context

    class Meta:
        verbose_name = "Список отелей"
        verbose_name_plural = "Списки отелей"
        ordering = ('-created_at',)
