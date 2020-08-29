from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from home.models import Order

from django.contrib import messages
import datetime

global thank        # becoz without this there was error of local storage assignment
global id
# Create your views here.
'''
                                    for passing variables 
def index(request) :
    context ={
         'variable1':"this is sent",
         'variable2':"this is sent by rahul"

    }
    return render(request,"index.html",context)
'''

def index(request) :
    return render(request,"index.html")
def services(request) :
    return HttpResponse("services")

def contact(request) :
    #making database model in model'py by name contact to link with view
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.date.today())
        contact.save()
        messages.success(request, 'Form Submitted!')      #needed to be iterate in template
    return render(request,"contact.html")

def me(request) :
    return render(request,"about.html")

def tracker(request):
    return render(request,"tracker.html")
def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        order= Order(amount=amount,items_json=items_json,name=name, email=email, phone=phone, address=address,city=city,zip_code=zip_code,state=state)
        order.save()
        thank = True

        id = order.order_id
        return render(request,"checkout.html",  {'thank': thank, 'id': id})
    return render(request, "checkout.html")