from django.shortcuts import render,redirect
from .forms import RegisterForm, LoginForm
from django.http import JsonResponse
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return redirect("posts:main_view")
    else:
        return render(request, "index.html")

def login_view(request):
    if request.user.is_authenticated:
        return redirect("posts:main_section")
    else:
        form = LoginForm()
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                password = form.cleaned_data["password"]
                username = form.cleaned_data["username"]

                user = authenticate(request, username = username, password = password)
                if user != None:
                    login(request, user)
                    return redirect("posts:main_view")
            else:
                messages.warning(request, "Invalid username or password")
        else:
            form = LoginForm()
        context = {
            "form": form
        }
        return render(request, "login.html", context)


def register_view(request):
    if request.user.is_authenticated:
        return redirect("posts:main_section")
    else:
        form = RegisterForm()
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Account Successfully Created. Please Login to Continue")
                return redirect("users:login_view")

            else:
                messages.warning(request,"Something is Wrong!! Please Try Again")
        
        else:
            form = RegisterForm()

        context = {
            "form":form
        }
        return render(request,"register.html", context)

@login_required(login_url="users:login_view")
def logout_view(request):
    logout(request)
    messages.success(request,"Logged Out successfully")
    return redirect("users:login_view")