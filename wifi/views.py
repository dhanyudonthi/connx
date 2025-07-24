from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def wifi_home(request):
    return render(request, 'wifi/home.html')  # Render WiFi template
