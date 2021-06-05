from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegisterForm, LoginForm, User_Edit_Form, Profile_Edit_Form
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
        return redirect("posts:main_view")
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
        return render(request, "users/login.html", context)


def register_view(request):
    if request.user.is_authenticated:
        return redirect("posts:main_view")
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
        return render(request,"users/register.html", context)

@login_required(login_url="users:login_view")
def logout_view(request):
    logout(request)
    messages.success(request,"Logged Out successfully")
    return redirect("users:login_view")



def profile_view(request, username):
    get_user = get_object_or_404(User, username = username)
    active_user = request.user
    user_form = User_Edit_Form(instance= active_user)
    profile_form = Profile_Edit_Form(instance=active_user.profile)

    if request.user == get_user:
        followed = "user"
    else:
        if active_user in get_user.profile.follower.all() and get_user in active_user.profile.following.all():
            followed = True
        else:
            followed = False

    context = {
        "get_user": get_user,
        "followed": followed,
        "user_form": user_form,
        "profile_form": profile_form
    }
    return render(request, "users/profile.html", context)



def follow_unfollow(request, username):
    get_user = get_object_or_404(User, username = username)
    active_user = request.user
    if active_user in get_user.profile.follower.all() and get_user in active_user.profile.following.all():
        followed = False
        active_user.profile.following.remove(get_user)
        get_user.profile.follower.remove(active_user)
    else:
        followed = True
        active_user.profile.following.add(get_user)
        get_user.profile.follower.add(active_user)
    data = {
        "followed": followed
    }
    return redirect("users:profile_view", username = username)



# def user_edit_view(request):

#     context = {
#         "user_form": user_form,
#         "profile_form": profile_form
#     }
#     return render(request, "users/profile.html",context)