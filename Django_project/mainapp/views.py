from random import choice

from django.core.cache import cache
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from mainapp.models import ProductCategory, Product
from shop import settings


def get_products():
    if settings.LOW_CACHE:
        key = "products"
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(
                is_active=True, category__is_active=True
            ).select_related("category")
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(
            is_active=True, category__is_active=True
        ).select_related("category")


def get_hot_product():
    # products = Product.objects.filter(is_active=True).all()
    return choice(get_products())


def index(request):
    context = {
        "page_title": "главная",
    }
    return render(request, "mainapp/index.html", context)


def catalog(request):
    hot_product = get_hot_product()

    context = {
        "page_title": "каталог",
        "hot_product": hot_product,
    }
    return render(request, "mainapp/catalog.html", context)


def product_page(request, pk):
    context = {
        "page_title": "товар",
        "product": get_object_or_404(Product, pk=pk),
    }
    return render(request, "mainapp/product_page.html", context)


def category(request, pk, page=1):  # категория продукта (каталог)
    if pk == 0:
        item = {"pk": 0, "name": "все"}
        products = get_products()
    else:
        item = get_object_or_404(ProductCategory, pk=pk)
        products = Product.objects.filter(category=item, is_active=True)

    products_paginator = Paginator(products, 3)
    try:
        products = products_paginator.page(page)
    except PageNotAnInteger:
        products = products_paginator.page(1)
    except EmptyPage:
        products = products_paginator.page(products_paginator.num_pages)

    context = {
        "page_title": "каталог",
        "item": item,
        "products": products,
    }
    return render(request, "mainapp/category.html", context)


def contacts(request):
    locations = [
        {
            "city": "г. Екатеринбург",
            "phone": "+7 (999) 999-99-99",
            "email": "shop@mail.ru",
            "address": "ул. Мира, д.1",
        },
        {
            "city": "г. Сысерть",
            "phone": "+7 (999) 999-99-98",
            "email": "shop1@domkol.ru",
            "address": "ул. Мира, д.2",
        },
    ]
    context = {
        "page_title": "контакты",
        "locations": locations,
    }
    return render(request, "mainapp/contacts.html", context)


def product_price(request, pk):
    if request.is_ajax():
        product = Product.objects.filter(pk=pk).first()
        return JsonResponse({"price": product and product_price or 0})
