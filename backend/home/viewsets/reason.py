from rest_framework import viewsets
from ..models import Reason
from ..serializers import ReasonSerializer


class ReasonViewSet(viewsets.ModelViewSet):
    queryset = Reason.objects.all()
    serializer_class = ReasonSerializer
