from django.shortcuts import render
from .models import ProductCategory, Product
from django.shortcuts import get_object_or_404
from basketapp.models import Basket
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random


main_links_menu = [
        {'href': 'main', 'name': 'Главная'},
        {'href': 'products:index', 'name': 'Продукты'},
        {'href': 'contact', 'name': 'Контакты'}
    ]


def get_basket_sum(request):
    basket = request.user.basket.all() if request.user.is_authenticated else []
    total = 0
    for product in basket:
        position = get_object_or_404(Product, pk=product.pk)
        total += position.price * product.quantity
    return total


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]

    
def get_same_products(hot_product):
    return Product.objects.filter(category=hot_product.category).\
                                    exclude(pk=hot_product.pk)[:3]

def main(request):
    title = 'Главная'
    basket = request.user.basket.all() if request.user.is_authenticated else []
    content = {
            'title': title,
            'links_menu': main_links_menu,
            'basket': basket            
        }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    title = 'Категории'
    categories = ProductCategory.objects.all()
    basket = request.user.basket.all() if request.user.is_authenticated else []
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'Все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')
        content = {
            'title': title,
            'links_menu': main_links_menu,
            'category': category,
            'products': products,
            'categories': categories,
            'basket': basket,
            'same_products': same_products,
            'hot_product': hot_product,
        }
        return render(request, 'mainapp/products.html', content)
    content = {
        'title': title,
        'links_menu': main_links_menu,
        'categories': categories,
        'basket': basket,
        'same_products': same_products,
        'hot_product': hot_product,
    }

    print(categories)
    return render(request, 'mainapp/catalog.html', content)


def contact(request):
    title = 'Контакты'
    basket = request.user.basket.all() if request.user.is_authenticated else []
    content = {
            'title': title,
            'links_menu': main_links_menu,
            'basket': basket
        }
    return render(request, 'mainapp/contacts.html', content)


def product(request, pk):
    title = 'продукты'

    content = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/product.html', content)


def products(request, pk=None, page=1):
    links_menu = ProductCategory.objects.filter(is_active=True)
    basket = getBasket(request.user)

    if pk is not None:
        if pk == 0:
            category = {
                'pk': 0,
                'name': 'все'
            }
            products = Product.objects.filter(is_active=True, \
                                                             category__is_active=True).order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk, \
                                                              is_active=True, category__is_active=True).order_by('price')

        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        title = 'продукты'
        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products_paginator,
            'basket': basket,
        }

        return render(request, 'mainapp/products_list.html', content)
