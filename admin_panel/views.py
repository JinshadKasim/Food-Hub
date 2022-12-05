from django.shortcuts import render,redirect
from user.models import Orders


# Create your views here.


def adminLogin(request):
    return render(request,'admin_panel/admin_login.html')


def adminDashboard(request):
    orders=Orders.objects.all()
    return render(request,'admin_panel/dashboard.html',({'data':orders}))

def updateData(request,id=0):
     Orders.objects.filter(id=id).update(status='Completed')
     return redirect('dashboard')

def cancelData(request,id=0):
     Orders.objects.filter(id=id).update(status='Canceled')
     return redirect('dashboard')