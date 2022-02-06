# notes/views.py
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
import logging
from comments.forms import CommentsForm
from comments.models import Commentaries
from posts.models import Post

logger = logging.getLogger(__name__)


def add_comments(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            post_id = Post.objects.get(id=request.POST.id)
            form = CommentsForm(request.POST, request.FILES)
            if form.is_valid():
                Commentaries.objects.create(name=request.user, post= post_id, **form.cleaned_data)
                return redirect("home")
        else:
            form = CommentsForm()
        return render(request, "add_comments.html", {"form": form})
    return redirect('home')


def delete_comment(request, comment_id):
    comment = get_object_or_404(Post, id=comment_id)
    logger.info(f"Note with id = {comment}, successfully deleted!")
    comment.delete()
    return HttpResponseRedirect(request.path_info)



