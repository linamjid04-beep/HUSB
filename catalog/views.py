from django.shortcuts import render

from core.site_config import BRANDS

from .models import Product, ProductCategory


def equipment(request):
    categories = ProductCategory.objects.filter(is_active=True).prefetch_related("products")
    products = Product.objects.filter(is_active=True).select_related("category")
    return render(
        request,
        "catalog/equipment.html",
        {
            "categories": categories,
            "products": products,
            "featured_products": products.filter(featured=True),
        },
    )


def sumitomo_partner(request):
    return render(
        request,
        "catalog/sumitomo.html",
        {"partner_name": BRANDS["fiber_partner_display_name"]},
    )
