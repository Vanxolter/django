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
                logger.info(row)
