from django.shortcuts import render,redirect
from .models import *
from registration.forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def service(request):
    return render(request, 'home/service.html')

def book(request):
    products=Product.objects.all()
    return render(request, 'home/book.html',{'products':products})

@login_required(login_url='/login')
def buy(request,p_id):
    products=Product.objects.filter(product_id=p_id)
    return render(request, 'home/book_now.html',{'product':products})
def buyfinal(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        form.save()
        return redirect("/")
    return redirect("/buy")

def contact(request):
    return render(request, 'home/contactus.html')