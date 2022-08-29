from tkinter import Variable
from django.shortcuts import render,HttpResponse
from .models import *


# Create your views here.
def index(request):
    # context = {
    #     "Variable1":"this is Anmol Rastogi",
    #     "Variable2":"this is shabnam "
    # }
    return render(request, 'index.html')
    # return HttpResponse("this is my home  page Anmol Rastogi")

def about(request):
    return render(request, 'about.html')
    

def services(request):
    return render(request, 'services.html')


def contact(request):
    if request.method =="POST":
        name=request.POST.get("name")
        number=request.POST.get("number")
        # print(name,number)
        obj = contactUs(name=name,number=number)
        obj.save()
        
        
    return render(request,"contectUs.html")



