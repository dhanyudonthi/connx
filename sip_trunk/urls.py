from django.urls import path
from . import views

urlpatterns = [
    path('', views.sip_trunk_home, name='sip_trunk_home'),
]
