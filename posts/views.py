from django.shortcuts import render
from .models import Post
# Create your views here.
def main_view(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, "main.html", context)