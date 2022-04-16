from rest_framework import serializers
from ..models import Hotel
from .feature import FeatureSerializer


class HotelSerializer(serializers.ModelSerializer):
    features = FeatureSerializer(many=True)

    class Meta:
        model = Hotel
        fields = '__all__'
