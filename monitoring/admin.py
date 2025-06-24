from django.contrib import admin
from .models import PoliceStation, CCTVArea, CCTV

@admin.register(PoliceStation)
class PoliceStationAdmin(admin.ModelAdmin):
    list_display = ['name', 'area']

@admin.register(CCTVArea)
class CCTVAreaAdmin(admin.ModelAdmin):
    list_display = ['name', 'police_station']

@admin.register(CCTV)
class CCTVAdmin(admin.ModelAdmin):
    list_display = ['ip_address', 'cctv_area', 'is_active']

