from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
import logging

from comments.models import Commentaries
from posts.forms import PostForm
from posts.models import Post

logger = logging.getLogger(__name__)


def main(request):
    '''posts = Post.objects.filter(author=request.user).order_by("-id")''' # Если я хочу вдеть посты АВТОРИЗОВАННОГО юзера
    posts = Post.objects.all # Если я хочу видеть посты ВСЕХ юзеров
    return render(request, "main.html", {"posts": posts})


def post_view(request, slug):
    post = Post.objects.get(slug=slug)
    comments = Commentaries.objects.filter(post=post) # Отображение комментариев только под теми постами к которым они были написаны
    return render(request, "view.html", {"post": post, "comments": comments})


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
    return redirect('home')


def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    logger.info(f"Note with id = {post}, successfully deleted!")
    post.delete()
    return redirect('home')