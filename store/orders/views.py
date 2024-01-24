from django.shortcuts import render

from django.views.generic import CreateView, TemplateView


class OrderCreateView(TemplateView):
    template_name = 'orders/order-create.html'
