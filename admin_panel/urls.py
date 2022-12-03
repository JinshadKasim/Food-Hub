from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_login',views.adminLogin,name='admin_login'),
    path('dashboard',views.adminDashboard,name='dashboard'),
]
