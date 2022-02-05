from django.db import models
from django.conf import settings
from posts.models import Post


class Commentaries(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete = models.CASCADE)
    name = models.CharField(settings.AUTH_USER_MODEL, max_length=200)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)