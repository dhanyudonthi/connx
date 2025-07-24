from django.urls import path
from . import views

urlpatterns = [
    path('', views.switches_home, name='switches_home'),
]
