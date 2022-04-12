from ..models.hotel_list_page import HotelListPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(HotelListPage)
class HotelListPageAdmin(BasePageAdmin):
    pass
