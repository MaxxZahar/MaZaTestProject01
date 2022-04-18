from django.db import models
from garpix_page.models import BaseListPage


class HotelListPage(BaseListPage):
    paginate_by = 5
    template = 'pages/hotel_list.html'

    def get_context(self, request=None, *args, **kwargs):
        from .hotel import Hotel
        from .feature import Feature
        from ..serializers import HotelSerializer, FeatureSerializer
        from ..settings import HOTEL_TYPES, NUMBER_OF_FEATURES_AT_TOP_FILTER

        context = super().get_context(request, *args, **kwargs)
        features = FeatureSerializer(Feature.objects.all()[:NUMBER_OF_FEATURES_AT_TOP_FILTER], many=True).data
        queryset = Hotel.objects.all()
        for element in HOTEL_TYPES:
            if request.GET.get(element[1], False):
                queryset = queryset.filter(type=element[0])
        for feature in features:
            if request.GET.get(feature['html_form_name'], False):
                queryset = queryset.filter(features__id__icontains=feature['id'])
        if request.GET.get('min-price', False):
            min_price = request.GET.get('min-price')
            queryset = queryset.filter(price__gte=min_price)
        if request.GET.get('max-price', False):
            max_price = request.GET.get('max-price')
            queryset = queryset.filter(price__lte=max_price)
        par = request.GET.get('ordering', False)
        ordering_set = {'price', 'type', 'rating'}
        ordering_set_reverse = {'-' + item for item in ordering_set}
        if par in ordering_set.union(ordering_set_reverse):
            queryset = queryset.order_by(par)

        total = len(queryset)
        pages = []
        i = 0
        j = 0
        data = []
        page = {}
        number = 1
        for item in queryset:
            data.append(item)
            i += 1
            j += 1
            if i == self.paginate_by:
                i = 0
                page['data'] = data
                page['number'] = number
                number += 1
                pages.append(page)
                page = {}
                data = []
            elif j == total:
                page['data'] = data
                page['number'] = number
                pages.append(page)
        page_number = 1

        if request.GET.get('page', False):
            try:
                page_number = int(request.GET.get('page'))
                if page_number > len(pages) or page_number < 1:
                    raise ValueError
            except ValueError:
                print('Wrong request')
            queryset = pages[page_number - 1]['data']
        else:
            queryset = pages[0]['data']

        page_range = list(range(1, len(pages) + 1))

        hotels = HotelSerializer(queryset, many=True).data

        context.update({
            'total': total,
            'hotels': hotels,
            'features': features,
            'hotel_types': HOTEL_TYPES,
            'page': page_number,
            'page_range': page_range,
        })
        for hotel in context['hotels']:
            hotel.update({'range': list(range(hotel['stars']))})

        return context

    class Meta:
        verbose_name = "Список отелей"
        verbose_name_plural = "Списки отелей"
        ordering = ('-created_at',)
