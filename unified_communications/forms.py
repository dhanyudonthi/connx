from django import forms
from .models import Estimate
from django.contrib.auth.forms import PasswordResetForm

class CreateEstimateForm(forms.ModelForm):
    class Meta:
        model = Estimate
        fields = ['name', 'email', 'estimate_name', 'intended_use']

# save password when resetting
class CustomPasswordResetForm(PasswordResetForm):
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
