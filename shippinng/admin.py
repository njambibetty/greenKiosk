from django.contrib import admin

# Register your models here.

from .models import Name, DispenserCoolerBox Product, Order

admin.site.register(Name)
admin.site.register(DispenserCoolerBox)
admin.site.register(Order)

