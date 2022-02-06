from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.comments.serializers import CommentsModelSerializer
from comments.models import Commentaries


class CommentsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed.
    """

    queryset = Commentaries.objects.all().order_by("-created")
    serializer_class = CommentsModelSerializer
    permission_classes = [IsAuthenticated]
