from django.shortcuts import render,redirect
from user.models import Orders
from admin_panel.models import Admin
from decorators import login_check,logout_check



# Create your views here.


@logout_check
def adminLogin(request):
    if request.method == 'POST':
            username = request.POST['user_name']
            password = request.POST['password']  
            try:
                adminObj = Admin.objects.get(user_name=username,password=password)
                # if user.email == username and user.password == password:
                request.session['adminId'] = adminObj.id
                print(request.session['adminId'])
                return redirect('dashboard')

            except:
                return render(request,'admin_panel/admin_login.html')

        
        # print(username)
        # print(password)
    return render(request,'admin_panel/admin_login.html')

def adminLogout(request):
    if 'adminId' in request.session:
        del  request.session['adminId']
        return render(request,'admin_panel/admin_login.html')
    return render(request,'admin_panel/admin_login.html')


@login_check
def adminDashboard(request):
        orders=Orders.objects.all()
        return render(request,'admin_panel/dashboard.html',({'data':orders}))


def updateData(request,id=0):
    print(id)
    Orders. objects.filter(id=id).update(status='Completed')
    print('in update data')
    return redirect('dashboard')

def cancelData(request,id=0):
     Orders.objects.filter(id=id).update(status='Canceled')
     return redirect('dashboard')

    