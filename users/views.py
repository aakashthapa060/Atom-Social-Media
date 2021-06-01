from django.shortcuts import render,redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
def register_view(request):
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