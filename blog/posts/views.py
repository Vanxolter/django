from django.http import HttpResponse
from django.shortcuts import render
import logging
from posts.models import Post

logger = logging.getLogger(__name__)

def posts_index(request):
    return render(request, 'main/posts.html')


# Вводим в url строку запрос в виде: title/?title='наш титл'
def search_by_title(request):
    value = request.GET.get("title")
    logger.info(f'Пользователь {request.user} ввел Get-запросом данный текст: {value}')
    single_post = Post.objects.filter(title = value).first()
    return HttpResponse(f" <h4>Титл '{value}' создан пользователем: {single_post.author}</h4> \n "
                        f"и имеет текст '{single_post.text}', время создания {single_post.created_at}")


# Работает кривовато, выводит первый пост, пробовал подставлять .all, при выводе выдает ошибку так как type(post_by_user) = class, засовывал в for и все безуспешно
def search_by_mainuser(request):
    post_by_user = Post.objects.filter(author=request.user).first()
    logger.info(f'Сейчас пользователь {request.user} попытался узнать свои посты')
    return HttpResponse(f'Все посты созданные пользователем {request.user}\n {post_by_user.title}')