from rest_framework import serializers

from comments.models import Commentaries


class CommentsModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Commentaries
        fields = ["name", "body"]