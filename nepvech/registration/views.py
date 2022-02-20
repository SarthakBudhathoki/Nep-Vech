from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm, LoginForm
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import auth

# Create your views here.
def signup(request):
 if request.method == "POST":
  fm = SignUpForm(request.POST)
  loginform = LoginForm(request=request, data=request.POST)
  if fm.is_valid():
   messages.success(request, 'Account Created Successfully !!') 
   fm.save()
   return redirect('login')
 else: 
  fm = SignUpForm()
  loginform = LoginForm()
 return render(request, 'registration/login.html', {'form':fm, 'loginform': loginform})

def logout(request):
    auth.logout(request)
    return redirect("/")

class LoginView(View):
    form_class = LoginForm
    template_name = 'registration/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        signupform = SignUpForm()
        return render(request, self.template_name, {'form':form, 'signupform': signupform})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request=request, data=request.POST)
        signupform = SignUpForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get('username')
            upass = form.cleaned_data.get('password')
            user = authenticate(username=uname, password=upass)
            if user is not None:
              login(request, user)
              messages.success(request, ('Logged In successfully!!'))
              return redirect('/')

        return render(request, self.template_name, {'form':form, 'signupform': signupform})