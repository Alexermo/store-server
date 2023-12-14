from django.urls import path

from .views import users

app_name = 'users'

urlpatterns = [
    path('users/', users, name='users'),
    path('users/register/', users, name='register'),
]
