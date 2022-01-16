from django.http import HttpResponse
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def posts_index(request):
    value = request.GET.get("key")
    logger.info(value)
    return render(request, 'main/posts.html')