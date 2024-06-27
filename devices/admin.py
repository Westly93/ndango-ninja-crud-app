from django.contrib import admin
from .models import Device, Location
# Register your models here.

admin.site.register(Location)
admin.site.register(Device)
