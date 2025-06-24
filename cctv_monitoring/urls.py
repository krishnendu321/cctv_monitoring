"""
URL configuration for cctv_monitoring project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from monitoring import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ Redirect root to dashboard (protected by login)
    path('', lambda request: redirect('dashboard')),

    # ✅ Auth Views

    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # ✅ App views
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/areas/', views.area_dashboard, name='area_dashboard'),

    # ✅ Include app URLs
    path('', include('monitoring.urls')),
    path('station/<int:ps_id>/cctvs/', views.station_cctvs, name='station_cctvs'),
]
