from rest_framework import serializers
from ..models import HomePage
from .reason import ReasonSerializer


class HomePageSerializer(serializers.ModelSerializer):
    reasons = ReasonSerializer(many=True)

    class Meta:
        model = HomePage
        fields = '__all__'
