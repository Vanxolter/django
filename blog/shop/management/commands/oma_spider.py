import logging
from pathlib import Path

import requests
from django.conf import settings

from django.core.management.base import BaseCommand

from shop.models import Product
from shop.spiders.spyders import OmaSpider
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from scrapy.utils.project import get_project_settings

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Crawl OMA catalog"

    def handle(self, *args, **options):
        def crawler_results(signal, sender, item, response, spider):
            item["cost"] = int(item["cost"].split(",")[0])
            if item["image"]:
                response = requests.get(item["image"])
                if response.ok:
                    path = Path(item["image"])
                    open(settings.MEDIA_ROOT / path.name, "wb").write(response.content)
                    item["image"] = path.name
            Product.objects.update_or_create(
                external_id=item["external_id"], defaults=item
            )

        dispatcher.connect(crawler_results, signal=signals.item_scraped)

        process = CrawlerProcess(get_project_settings())
        process.crawl(OmaSpider)
        process.start()
