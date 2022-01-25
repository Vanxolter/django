from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
import logging

from posts.forms import PostForm
from posts.models import Post

logger = logging.getLogger(__name__)


def main(request):
    return render(request, "main.html")


def posts_index(request):
    result = ""
    author_name = request.GET.get("author", "maksim")
    for x in Post.objects.filter(author__username=author_name).order_by("-id"):
        result += f"<div style='border: 2px solid black'>"
        result += f"<h1>{x.title} #{x.id}</h1>"
        result += f"<div>{x.text}</div>"
        result += f"</div></br>"


def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            logger.info(form.cleaned_data)
            post = Post(
                author=request.user,
                title=form.cleaned_data['title'],
                image=form.cleaned_data['image'],
                slug=form.cleaned_data['slug'],
                text=form.cleaned_data['text'])
            post.save()
            return redirect("/")
    else:
        form = PostForm()
    return render(request, "add_posts.html", {"form": form})