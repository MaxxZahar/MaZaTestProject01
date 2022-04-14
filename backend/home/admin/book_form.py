from django.contrib import admin
from ..models import BookFormModel


@admin.register(BookFormModel)
class BookFormModelAdmin(admin.ModelAdmin):
    exclude = ('created_at',)