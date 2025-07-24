from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def sdwan_home(request):
    return render(request, 'sdwan/home.html')  # Render SDWAN template
