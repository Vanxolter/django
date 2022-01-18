from django.http import HttpResponse
from django.shortcuts import render
import logging
from posts.models import Post

logger = logging.getLogger(__name__)

def posts_index(request):
    return render(request, 'main/posts.html')


def search_by_title(request):
    value = request.GET.get("title")
    logger.info(value)
    single_post = Post.objects.filter(title = value).first()
    return HttpResponse(f" <h4>Титл '{value}' создан пользователем: {single_post.author}</h4> \n "
                        f"и имеет текст '{single_post.text}', время создания {single_post.created_at}")