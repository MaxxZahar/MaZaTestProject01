from rest_framework import serializers
from ..models import Reason
from .recommendation import RecommendationSerializer


class ReasonSerializer(serializers.ModelSerializer):
    reason_recommendation = RecommendationSerializer(read_only=True, many=True)

    class Meta:
        model = Reason
        depth = 1
        fields = ('id', 'title', 'number', 'description', 'css_class', 'reason_recommendation')
