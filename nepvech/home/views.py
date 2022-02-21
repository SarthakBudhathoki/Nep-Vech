from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import ContactForm,ProductForm
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
    if request.method=="POST":
        form=ContactForm(request.POST)
        form.save()
        messages.info(request,"your message was sent")
        return redirect("/contact")
    return render(request, 'home/contactus.html')

def admin(request):
    booking=Booking.objects.all()
    return render(request,'home/admin.html',{'bookings':booking})

def addproduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            try:
                print("valid")
                form.save()
                return redirect("/admin")
            except:
                print("Failed")
    else:
        form = ProductForm()
        print("invalid")
    return render(request, 'home/addproduct.html',{'form':form})

def viewmessage(request):
    contacts=Contact.objects.all()
    return render(request,"home/display.html",{'contacts':contacts})