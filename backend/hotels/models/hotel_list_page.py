from django.db import models
from garpix_page.models import BaseListPage


class HotelListPage(BaseListPage):
    paginate_by = 2
    template = 'pages/hotel_list.html'

    def get_context(self, request=None, *args, **kwargs):
        from .hotel import Hotel
        from .feature import Feature
        from ..serializers import HotelSerializer, FeatureSerializer
        from ..settings import HOTEL_TYPES, NUMBER_OF_FEATURES_AT_TOP_FILTER
        context = super().get_context(request, *args, **kwargs)
        queryset = Hotel.objects.all()
        par = request.GET.get('ordering', False)
        ordering_set = {'price', 'type', 'rating'}
        ordering_set_reverse = {'-' + item for item in ordering_set}
        if par in ordering_set.union(ordering_set_reverse):
            queryset = queryset.order_by(par)
        hotels = HotelSerializer(queryset, many=True).data
        features = FeatureSerializer(Feature.objects.all()[:NUMBER_OF_FEATURES_AT_TOP_FILTER], many=True).data
        context.update({
            'hotels': hotels,
            'features': features,
            'hotel_types': HOTEL_TYPES,
        })
        for hotel in context['hotels']:
            hotel.update({'range': list(range(hotel['stars']))})
        return context

    class Meta:
        verbose_name = "Список отелей"
        verbose_name_plural = "Списки отелей"
        ordering = ('-created_at',)
