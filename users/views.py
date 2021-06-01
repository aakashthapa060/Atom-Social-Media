from django.shortcuts import render,redirect
from .forms import RegisterForm, LoginForm
from django.http import JsonResponse
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

def index(request):
    return render(request, "index.html")
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data["password"]
            username = form.cleaned_data["username"]

            user = authenticate(request, username = username, password = password)
            if user != None:
                login(request, user)
                print("hello")
        else:
            messages.warning(request, "Invalid username or password")
    else:
        form = LoginForm()
    context = {
        "form": form
    }
    return render(request, "login.html", context)


def register_view(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.warning(request,"Something is Wrong!! Please Try Again")
    
    else:
        form = RegisterForm()
    
    context = {
        "form":form
    }
    return render(request,"register.html", context)

