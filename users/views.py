from django.shortcuts import render
from .forms import RegisterForm, LoginForm
# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegisterForm()
    context = {
        "form": form
    }
    return render(request, "index.html", context)