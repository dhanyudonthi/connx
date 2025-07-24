from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('unified_communications/', include('unified_communications.urls')),
    path('contact_center/', include('contact_center.urls')),
    path('sdwan/', include('sdwan.urls')),
    path('switches/', include('switches.urls')),
    path('wifi/', include('wifi.urls')),
    path('sip_trunk/', include('sip_trunk.urls')),
    path('', include('unified_communications.urls')),  # Ensure this is included last
]
