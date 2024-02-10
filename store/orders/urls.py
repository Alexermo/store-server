from django.urls import path

from .views import (OrderCancelView, OrderCreateView, OrderDetailView,
                    OrderListView, OrderSuccessView)

app_name = 'orders'

urlpatterns = [
    path('order-create/', OrderCreateView.as_view(), name='order_create'),
    path('order-success/', OrderSuccessView.as_view(), name='order_success'),
    path('order-canceled/', OrderCancelView.as_view(), name='order_canceled'),
    path('orders/', OrderListView.as_view(), name='orders_list'),
    path('order/<int:pk>', OrderDetailView.as_view(), name='order_detail'),
]
