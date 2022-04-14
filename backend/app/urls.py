from garpixcms.urls import *  # noqa
from django.urls import path, include
from . import views

urlpatterns = [path('blank/', views.blank, name='blank'),
               path('api/v1/booking/', include('home.urls'))] + urlpatterns  # noqa
