from rest_framework import serializers
from ..models import HotelListPage


class HotelListPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelListPage
        fields = '__all__'

