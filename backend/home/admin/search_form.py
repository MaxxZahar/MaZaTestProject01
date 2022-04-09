from django.contrib import admin
from ..models import SearchFormModel


@admin.register(SearchFormModel)
class SearchFormModelAdmin(admin.ModelAdmin):
    list_display = ('arrival_date', 'departure_date', 'number_of_adults', 'number_of_children')

