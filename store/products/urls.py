from django.urls import path

from .views import index, products, basket_add, basket_delete

app_name = 'products'

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products'),
    path('page/<int:page_number>', products, name='paginator'),
    path('products/category/<int:category_id>/', products, name='category'),
    path('products/basket/<int:product_id>/', basket_add, name='basket_add'),
    path('products/basket_delete/<int:basket_id>/',
         basket_delete, name='basket_delete'),
]
