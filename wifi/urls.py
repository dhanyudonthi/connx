from django.urls import path
from . import views

urlpatterns = [
    path('', views.wifi_home, name='wifi_home'),
]
