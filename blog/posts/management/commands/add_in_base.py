from django.core.management.base import BaseCommand

from blog import settings
from posts.models import Post
import logging
import csv

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "All my poata"

    def handle(self, *args, **options):
        with open(settings.BASE_DIR / "posts.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                Post.objects.create(title=row[1], image= None, slug=row[2], text=row[3], created_at=row[4], author_id=row[5])
