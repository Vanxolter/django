from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
import logging
from posts.models import Post

logger = logging.getLogger(__name__)


def posts_index(request):
    result = ""
    author_name = request.GET.get("author", "maksim")
    for x in Post.objects.filter(author__username=author_name).order_by("-id"):
        result += f"<div style='border: 2px solid black'>"
        result += f"<h1>{x.title} #{x.id}</h1>"
        result += f"<div>{x.text}</div>"
        result += f"</div></br>"
    return HttpResponse(result)


# Вводим в url строку запрос в виде: title/?title='наш титл'
def search_by_title(request):
    result = ""
    value = request.GET.get("title")
    logger.info(f'Пользователь {request.user} ввел Get-запросом данный текст: {value}')
    for x in Post.objects.filter(title=value).order_by("-id"):
        result += f"<div style='border: 2px solid black'>"
        result += f"<h1>{x.title} #{x.id}</h1>"
        result += f"<div>{x.text}</div>"
        result += f"</div></br>"
    return HttpResponse(result)


# Работает кривовато, выводит первый пост, пробовал подставлять .all, при выводе выдает ошибку так как type(post_by_user) = class, засовывал в for и все безуспешно
def search_by_mainuser(request):
    post_by_user = Post.objects.filter(author=request.user).first()
    logger.info(f'Сейчас пользователь {request.user} попытался узнать свои посты')
    return HttpResponse(f'Все посты созданные пользователем {request.user}\n {post_by_user.title}')