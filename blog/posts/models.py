from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts"
    )
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    text = models.TextField(help_text="Введите ваш текст")
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)


class Tags(models.Model):
    title = models.CharField(max_length=100)
    posts = models.ManyToManyField(Post)
