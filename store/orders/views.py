from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic import CreateView

from .forms import OrderForm

from common.view import TitleMixin


class OrderCreateView(TitleMixin, CreateView):
    template_name = 'orders/order-create.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:order_create')
    title = 'Store - Order'

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)
