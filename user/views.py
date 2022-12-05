from django.shortcuts import render
from user.models import Orders


# Create your views here.

def index(request):
     if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['number']
        address = request.POST['address']
        food_details = request.POST['food_details']
        status = request.POST['status']
        orderObj = Orders(name=name, number=number, address=address, food_details=food_details, status=status)
        orderObj.save()
        return render(request,'user/thankyou.html')
        
     return render(request,'user/index.html')