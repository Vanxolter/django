from django.core.paginator import Paginator
from django.db.models import Sum, F
from django.shortcuts import render, redirect, get_object_or_404
import logging

from shop.forms import PurchaseFilterForm, ProdFiltersForm
from shop.models import Product, Purchase

logger = logging.getLogger(__name__)


# ГЛАВНАЯ СТРАНИЦА МАГАЗИНА
def product_list(request):
    products = Product.objects.all()
    filters_form = ProdFiltersForm(request.GET)

    if filters_form.is_valid():
        cost__gt = filters_form.cleaned_data["cost__gt"]
        if cost__gt:
            products = products.filter(cost__gt=cost__gt)

        cost__lt = filters_form.cleaned_data["cost__lt"]
        if cost__lt is not None:
            products = products.filter(cost__lt=cost__lt)

        order_by = filters_form.cleaned_data["order_by"]
        if order_by:
            if order_by == "cost_asc":
                products = products.order_by("cost")
            if order_by == "cost_desc":
                products = products.order_by("-cost")
            if order_by == "max_count":
                products = products.annotate(
                    total_count=Sum("purchases__count").order_by("-total_count")
                )
            if order_by == "max_price":
                products = products.annotate(
                    total_cost=Sum("purchases_count") * F("cost")
                ).order_by("-total_cost")

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
            Purchase.objects.create(
                product=product, user=request.user, count=request.POST.get("count")
            )
            return redirect("product_details_view", product_id=product_id)
    return render(request, "products/details.html", {"product": product})