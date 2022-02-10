
from django.shortcuts import render, redirect
import logging
from shop.models import Product, Purchase

logger = logging.getLogger(__name__)


# ГЛАВНАЯ СТРАНИЦА С ФОРМОЙ ДОБАВЛЕНИЯ ПОСТА И ВЫВОДОМ ВСЕХ ПОСТОВ
def product_list(request):
    products = Product.objects.order_by('-id')
    return render(request, "products/products.html", {"products": products})




