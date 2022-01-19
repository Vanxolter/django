from django.db import models
from django.conf import settings


class User(models.Model):
    email = models.CharField(max_length=20)
    name = models.CharField(max_length=15, help_text='Обязательно к заполнению')
    surname = models.CharField(max_length=15, help_text='Обязательно к заполнению')
    age = models.CharField(max_length=3)
    sex = models.TextField(choices=[('ж', 'Жэнтельмен'), ('м', 'Мадмуазель')])
    image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)