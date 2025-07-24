from django.db import models
import uuid
from django.contrib.auth.models import User
import string,random
from django.db import models
from django.conf import settings
from decimal import Decimal
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    INTERNAL = 'internal'
    EXTERNAL = 'external'

    USER_LEVEL_CHOICES = [
        (INTERNAL, 'Internal'),
        (EXTERNAL, 'External'),
    ]

    user_level = models.CharField(
        max_length=10,
        choices=USER_LEVEL_CHOICES,
        default=INTERNAL,  # Set default value
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        db_table = 'public.user_profiles'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, user_level=UserProfile.EXTERNAL)  # Set default user level


class switches(models.Model):
    sku = models.CharField(max_length=255)
    description = models.TextField()
    list_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # List price for wholesale

    def __str__(self):
        return f"{self.sku} - {self.description}"

    class Meta:
        db_table = 'switches'

class WebexContactCenter(models.Model):
    sku = models.CharField(max_length=255)
    description = models.TextField()
    list_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # List price for wholesale

    def __str__(self):
        return f"{self.sku} - {self.description}"

    class Meta:
        db_table = 'ccaas.webex_contact_center'

class WebexCallingWholesale(models.Model):
    sku = models.CharField(max_length=255)
    description = models.TextField()
    list_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # List price for wholesale

    def __str__(self):
        return f"{self.sku} - {self.description}"

    class Meta:
        db_table = 'ucaas.webex_calling_wholesale'


class WebexCallingFlex(models.Model):
    sku = models.CharField(max_length=255)
    description = models.TextField()
    list_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # List price for flex

    def __str__(self):
        return f"{self.sku} - {self.description}"

    class Meta:
        db_table = 'ucaas.webex_calling_flex'


class WebexCallingOnPremHybrid(models.Model):
    sku = models.CharField(max_length=255)
    description = models.TextField()
    list_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # List price for on-prem

    def __str__(self):
        return f"{self.sku} - {self.description}"

    class Meta:
        db_table = 'ucaas.webex_calling_onprem_hybrid'


# Calculate pricing model
class SalesPricing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sales_pricings',null= True)
    mfg_part_number = models.CharField(max_length=255)
    description = models.TextField()
    qty = models.IntegerField()
    term_in_months = models.IntegerField(null=True, blank=True)
    list_cost = models.DecimalField(max_digits=10, decimal_places=2)
    connx_std_discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    deal_specific_discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    connx_std_gross_margin = models.DecimalField(max_digits=5, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    adjusted_gross_margin_percent = models.DecimalField(max_digits=5, decimal_places=2)
    ext_unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ext_total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    item_type = models.CharField(max_length=255, default="placeholder")

    USERNAME_FIELD = 'user'


    def __str__(self):
        return f"{self.mfg_part_number} - {self.description}"

    class Meta:
        db_table = 'ucaas.sales_pricing'


class Estimate(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    estimate_name = models.CharField(max_length=255)
    intended_use = models.TextField(blank=True, null=True)
    unique_id = models.CharField(
        max_length=10, 
        unique=True, 
        default='', 
        editable=False
    )  # 10-character unique ID
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = self.generate_unique_id()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_unique_id():
        while True:
            unique_id = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            if not Estimate.objects.filter(unique_id=unique_id).exists():
                return unique_id




class ProfessionalService(models.Model):
    SKU = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255)
    size_range_start = models.IntegerField(null=True, blank=True)  # Range start for size (e.g., 1)
    size_range_end = models.IntegerField(null=True, blank=True)    # Range end for size (e.g., 50)
    efforts_in_days = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Efforts can be optional
    inital_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Cost for the service
    calculated_cost=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantity=models.IntegerField(null=True, blank=True)
    def __str__(self):
        size_range = f"{self.size_range_start}-{self.size_range_end}" if self.size_range_start and self.size_range_end else "N/A"
        return f"{self.SKU} - {self.description} (Size Range: {size_range}, Cost: {self.cost})"


class SKU(models.Model):
    category = models.CharField(max_length=255)  # Level 1
    subcategory = models.CharField(max_length=255, blank=True, null=True)  # Level 2
    product_family = models.CharField(max_length=255, blank=True, null=True)  # Level 3
    product_type = models.CharField(max_length=255, blank=True, null=True)  # Level 4
    product_name = models.CharField(max_length=255, blank=True, null=True)
    sku = models.CharField(max_length=255, blank=True, null=True, unique=True)  # Level 5
    description = models.TextField(blank=True, null=True)
    list_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        unique_together = ('category', 'subcategory', 'product_family', 'product_type','product_name', 'sku')
    
    def __str__(self):
        return f"{self.category} > {self.subcategory or ''} > {self.product_family or ''} > {self.product_type or ''} > {self.product_name or ''} > {self.sku or ''}"

