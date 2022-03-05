from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
import logging
from django.contrib.auth.models import User

from django.views.generic import TemplateView

from shop.forms import ProdFiltersForm, PurchaseFilterForm
from shop.models import Product, Purchase
from shop.queries import filter_products, filter_purchases

logger = logging.getLogger(__name__)


# ГЛАВНАЯ СТРАНИЦА МАГАЗИНА
def product_list(request):
    products = Product.objects.all().order_by("id")
    filters_form = ProdFiltersForm(request.GET)

    if filters_form.is_valid():
        cost__gt = filters_form.cleaned_data["cost__gt"]
        cost__lt = filters_form.cleaned_data["cost__lt"]
        order_by = filters_form.cleaned_data["order_by"]

        products = filter_products(products, cost__gt, cost__lt, order_by)

    paginator = Paginator(products, 30)
    page_number = request.GET.get("page")
    products = paginator.get_page(page_number)

    return render(
        request,
        "products/products.html",
        {"filters_form": filters_form, "products": products},
    )


def product_details_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        if request.POST.get("count"):
            pur = Purchase.objects.create(
                product=product, user=request.user, count=request.POST.get("count")
            )
            logger.info(f"{request.user} added a new purchase - {pur.product} ")
            return redirect("product_details_view", product_id=product_id)
    return render(request, "products/details.html", {"product": product})


def purchase_list(request):
    products = Product.objects.filter(purchase__user=request.user)
    purchases = Purchase.objects.filter(user_id=request.user)
    logger.info(f"{request.user} have - {purchases} ")
    filters_form = PurchaseFilterForm(request.GET)

    if filters_form.is_valid():
        order_by = filters_form.cleaned_data["order_by"]

        purchases = filter_purchases(purchases, order_by)

    return render(
        request,
        "products/purchases.html",
        {"filters_form": filters_form, "purchases": purchases},
    )