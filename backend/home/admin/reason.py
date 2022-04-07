from django.contrib import admin
from ..models import Reason, Recommendation


class RecommendationInline(admin.TabularInline):
    model = Recommendation
    fk_name = 'reason'
    extra = 1


@admin.register(Reason)
class ReasonAdmin(admin.ModelAdmin):
    list_display = ('number', 'title')
    inlines = (RecommendationInline, )

