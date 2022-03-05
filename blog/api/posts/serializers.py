from rest_framework import serializers

from posts.models import Post


class PostModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "slug", "title", "image", "text", "created_at"]
