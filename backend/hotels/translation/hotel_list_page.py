from modeltranslation.translator import TranslationOptions, register
from ..models import HotelListPage


@register(HotelListPage)
class HotelListPageTranslationOptions(TranslationOptions):
    pass
