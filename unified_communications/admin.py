from django.contrib import admin
from .models import UserProfile, WebexCallingWholesale, WebexCallingFlex, WebexCallingOnPremHybrid, SalesPricing, ProfessionalService, WebexContactCenter

admin.site.register(UserProfile)
admin.site.register(WebexCallingWholesale)
admin.site.register(WebexCallingFlex)
admin.site.register(WebexCallingOnPremHybrid)
admin.site.register(SalesPricing)
admin.site.register(ProfessionalService)
admin.site.register(WebexContactCenter)