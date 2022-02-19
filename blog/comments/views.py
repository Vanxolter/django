# notes/views.py
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
import logging
from comments.forms import CommentsForm
from comments.models import Commentaries
from posts.models import Post

logger = logging.getLogger(__name__)


# УДАЛЕНИЕ КОММЕНТА
def delete_comment(request, comment_id):
    comment = get_object_or_404(Commentaries, id=comment_id)
    logger.info(f"Note with id = {comment}, successfully deleted!")
    comment.delete()
    return HttpResponseRedirect(request.path_info)  # под вопросом НЕ ПРОХОДИТ УДАЛЕНИЕ
