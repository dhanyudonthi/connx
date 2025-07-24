from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def sip_trunk_home(request):
    return render(request, 'sip_trunk/home.html')  # Render SIP Trunk template
