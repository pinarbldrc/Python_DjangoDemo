from django.shortcuts import render
from .forms import RegisterForm

def register(request):

    form=RegisterForm()
    context={
        "form": form
    }
    return render(request,"registrations/register.html",context)

def login(request):
    return render(request,"registrations/login.html")

def logout(request):
    pass
# Create your views here.
