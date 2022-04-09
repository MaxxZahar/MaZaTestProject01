from django.forms import ModelForm
from ..models import SearchFormModel


class SearchForm(ModelForm):
    class Meta:
        model = SearchFormModel
        fields = ('arrival_date', 'departure_date', 'number_of_adults', 'number_of_children')
