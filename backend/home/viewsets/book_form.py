from rest_framework import viewsets, mixins
from ..serializers import BookFormModelSerializer
from rest_framework.response import Response
from rest_framework import status


class BookFormModelViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = BookFormModelSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        booking = serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
