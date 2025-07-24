from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def switches_home(request):
    return render(request, 'switches/home.html')  # Render Switches template
