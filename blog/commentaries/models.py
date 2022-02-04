from django.db import models
from django.conf import settings
from posts.models import Post


class Commentaries(models.Model):
    author = models.CharField(settings.AUTH_USER_MODEL, max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(help_text="Введите ваш текст")
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)