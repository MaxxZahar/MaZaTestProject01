from django.db import models
from garpix_page.models import BasePage


class BlankPage(BasePage):
    template = "pages/blank.html"

    class Meta:
        verbose_name = "Заглушка"
        verbose_name_plural = "Заглушки"
        ordering = ("-created_at",)
