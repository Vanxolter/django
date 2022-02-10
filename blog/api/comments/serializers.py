from rest_framework import serializers

from comments.models import Commentaries


class CommentsModelSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.HyperlinkedRelatedField(view_name="api:post-detail", read_only=True)

    class Meta:
        model = Commentaries
        fields = ["post", "name", "body"]