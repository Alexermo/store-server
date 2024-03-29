# from typing import Any
# from django.db.models.query import QuerySet
from django.contrib.auth.decorators import login_required
# from django.core.cache import cache
from django.shortcuts import HttpResponseRedirect
from django.views.generic import ListView, TemplateView

from common.view import TitleMixin

# from django.shortcuts import render
from .models import Basket, Product, ProductCategory

# from django.core.paginator import Paginator


class IndexView(TitleMixin, TemplateView):
    template_name = "products/index.html"
    title = 'Store'
# def index(request):
#     context = {
#         'title': 'Store',
#     }
#     return render(request, "products/index.html", context)


class ProductsListView(TitleMixin, ListView):
    model = Product
    template_name = "products/products.html"
    paginate_by = 3
    title = 'Store - Каталог'

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        context['categories'] = ProductCategory.objects.all()
        context['category_id'] = self.kwargs.get('category_id')
        # вариант кэширования
        # context['categories'] = cache.get_or_set(
        #     'categories', ProductCategory.objects.all(), 30)
        # выше короткий код для кода ниже
        # categories = cache.get('categories')
        # if categories:
        #     context['categories'] = categories
        # else:
        #     cache.set('categories', ProductCategory.objects.all(), 30)
        #     context['categories'] = cache.get('categories')
        return context


# def products(request, category_id=None, page_number=1):
#     products = Product.objects.filter(
#         category_id=category_id) if category_id else Product.objects.all()

#     per_page = 3
#     paginator = Paginator(products, per_page)
#     products_paginator = paginator.page(page_number)

#     context = {
#         'title': 'Store - Каталог',
#         'categories': ProductCategory.objects.all(),
#         'products': products_paginator,
#     }
#     return render(request, "products/products.html", context)


@login_required
def basket_add(request, product_id):
    Basket.create_or_update(product_id, request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_delete(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
