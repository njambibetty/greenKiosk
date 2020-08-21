from django.contrib import admin

# Register your models here.
from .models import Kiosk, KioskOwner

admin.site.register(KioskOwner)
admin.site.register(Kiosk)
