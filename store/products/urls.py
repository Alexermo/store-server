from django.urls import path

from .views import IndexView, ProductsListView, basket_add, basket_delete

# from django.views.decorators.cache import cache_page


app_name = 'products'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # кэш для всей страницы
    # path('', cache_page(15)(IndexView.as_view()), name='index'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('page/<int:page>', ProductsListView.as_view(), name='paginator'),
    path('products/category/<int:category_id>/',
         ProductsListView.as_view(), name='category'),
    path('products/basket/<int:product_id>/', basket_add, name='basket_add'),
    path('products/basket_delete/<int:basket_id>/',
         basket_delete, name='basket_delete'),
]
