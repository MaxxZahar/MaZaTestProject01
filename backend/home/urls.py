from rest_framework import routers
from .viewsets import BookFormModelViewSet

book_router = routers.DefaultRouter()
book_router.register('', BookFormModelViewSet, basename='BookFormModel')

urlpatterns = []
urlpatterns += book_router.urls

