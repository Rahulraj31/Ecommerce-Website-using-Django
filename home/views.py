from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
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
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Form Submitted!')      #needed to be iterate in template
    return render(request,"contact.html")

def me(request) :
    return render(request,"about.html")