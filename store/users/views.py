from django.shortcuts import render
from .models import User


def users(request):
    context = {
        'title': 'Store',
    }
    return render(request, "users/login.html", context)


def register(request):
    context = {
        'title': 'Store',
    }
    return render(request, "users/register.html", context)
