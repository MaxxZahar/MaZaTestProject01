from rest_framework import serializers
from ..models import BookFormModel


class BookFormModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookFormModel
        exclude = ('created_at', )
