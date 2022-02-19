import logging

from shop.models import Product
logger = logging.getLogger(__name__)


for i in Product.objects.all():
    logger.info(i.cost)