from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
import logging

from posts.forms import PostForm
from posts.models import Post

logger = logging.getLogger(__name__)


def main(request):
    posts = Post.objects.filter(author=request.user).order_by("-id")
    return render(request, "main.html", {"posts": posts})


def post_view(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "view.html", {"post": post})


def add_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                Post.objects.create(author=request.user, **form.cleaned_data)
                return redirect("home")
        else:
            form = PostForm()
        return render(request, "add_posts.html", {"form": form})
    return HttpResponse("You don't authenticated!")