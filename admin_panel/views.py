from django.shortcuts import render

# Create your views here.


def adminLogin(request):
    return render(request,'admin_panel/admin_login.html')


def adminDashboard(request):
    return render(request,'admin_panel/dashboard.html')
