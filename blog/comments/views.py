# notes/views.py
from django.shortcuts import render, redirect
import logging
from comments.forms import CommentsForm
from comments.models import Commentaries
from posts.models import Post

logger = logging.getLogger(__name__)


def add_comments(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CommentsForm(request.POST, request.FILES)
            if form.is_valid():
                Commentaries.objects.create(name=request.user, **form.cleaned_data)
                return redirect("home")
        else:
            form = CommentsForm()
        return render(request, "add_comments.html", {"form": form})
    return redirect('home')