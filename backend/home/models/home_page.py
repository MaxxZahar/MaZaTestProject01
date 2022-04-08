from django.db import models
from garpix_page.models import BasePage


class HomePage(BasePage):
    template = "pages/home.html"

    def get_context(self, request=None, *args, **kwargs):
        from .reason import Reason
        from ..serializers import ReasonSerializer
        context = super().get_context(request, *args, **kwargs)
        reasons = ReasonSerializer(Reason.objects.all(), many=True).data
        context.update({
            'reasons': reasons
        })
        return context

    # def get_serializer(self):
    #     from ..serializers import HomePageSerializer
    #     return HomePageSerializer

    class Meta:
        verbose_name = "Главная"
        verbose_name_plural = "Главная"
        ordering = ("-created_at",)
