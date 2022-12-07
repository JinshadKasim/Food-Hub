from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_login',views.adminLogin,name='admin_login'),
    path('admin_logout',views.adminLogout,name='admin_logout'),
    path('dashboard',views.adminDashboard,name='dashboard'),
    path('complete_data/<int:id>',views.updateData,name='complete_data'),
    path('cancel_data/<int:id>',views.cancelData,name='cancel_data'),
]
