import logging
from pathlib import Path
from time import sleep

import requests
from django.db.models import F
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher

from django_rq import job
from scrapy.utils.project import get_project_settings

from blog import settings
from shop.models import Product
from shop.spyders import OmaSpider
from scrapy import signals
logger = logging.getLogger(__name__)


@job
def run_products_update():
    Product.objects.filter(cost=0).update(status="OUT_OF_STOCK")


def some_view_or_function():
    run_products_update.delay()


@job
def run_oma_spider():

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


def some_run_spider():
    run_oma_spider.delay()


@job
def run_currency_bun_usd():

    # Ссылка с апи ключем
    url = 'https://api.currconv.com/api/v7/convert?q=USD_BYN&compact=ultra&apiKey=0962617823ff1e2471ed'

    # Достаю данные через request
    response = requests.get(url)
    data = response.json()

    # Достаю из дикта курс доллара
    coefficient = data.get("USD_BYN")
    Product.objects.all().update(price_byn=F('cost') * coefficient)
    '''for step in Product.objects.all():
        cost = step.cost
        Product.objects.filter(external_id= step.external_id).update(price_byn= coefficient * cost)'''


def update_price():
    run_currency_bun_usd.delay()