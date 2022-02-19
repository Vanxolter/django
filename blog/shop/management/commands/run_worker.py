from django.core.management.base import BaseCommand

import logging

from shop.redis import some_view_or_function, some_run_spider, update_price


class Command(BaseCommand):
    help = "Run worker"

    def handle(self, *args, **options):
        update_price()
