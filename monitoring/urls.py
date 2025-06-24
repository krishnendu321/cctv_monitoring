from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('map/', views.map_page, name='map_page'),
    path('station/<int:ps_id>/cctvs/', views.station_cctvs, name='station_cctvs'),
    path('area/<int:area_id>/map/', views.cctv_area_map, name='cctv_area_map'),
]
