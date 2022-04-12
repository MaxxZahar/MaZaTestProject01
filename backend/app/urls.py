from garpixcms.urls import *  # noqa
from django.urls import path
from . import views

urlpatterns = [path('blank/', views.blank, name='blank')] + urlpatterns  # noqa
