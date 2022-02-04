from django.core.management.base import BaseCommand

from blog import settings
from posts.models import Post
import logging
import csv

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "All my poata"

    def handle(self, *args, **options):
        with open(settings.BASE_DIR / "posts.csv", "w") as file:
            writer = csv.writer(file)
            for post in Post.objects.all():
                writer.writerow([post.id, post.title, post.slug, post.text, post.created_at, post.author_id])