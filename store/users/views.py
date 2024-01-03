from typing import Any
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy

from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LoginView

from .form import UserLoginForm, UserRegistrationForm, UserProfileForm

from django.views.generic import CreateView, UpdateView

from products.models import Basket
from users.models import User


class UserLoginView(LoginView):
    template_name = "users/login.html"
    form_class = UserLoginForm

# def login(request):
#     if request.method == "POST":
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('products:index'))
#     else:
#         form = UserLoginForm()
#     context = {'form': form}
#     return render(request, "users/login.html", context)


class UserRegistrationView(CreateView):
    model = User
    template_name = "users/register.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Вы успешно зарегестрированы!')
        return response

# def register(request):
#     if request.method == "POST":
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(
#                 request, 'Вы успешно зарегестрированы!')
#             return HttpResponseRedirect(reverse('products:index'))
#     else:
#         form = UserRegistrationForm()
#     context = {'form': form}
#     return render(request, "users/register.html", context)


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = "users/profile.html"

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context['title'] = 'Store - Личный кабинет'
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context

    def get_object(self, queryset=None):
        return self.request.user


# @login_required
# def profile(request):
#     if request.method == "POST":
#         form = UserProfileForm(instance=request.user,
#                                data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('users:profile'))
#     else:
#         form = UserProfileForm(instance=request.user)

#     context = {
#         'form': form,
#         'baskets': Basket.objects.filter(user=request.user)}
#     return render(request, 'users/profile.html', context)


# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse('products:index'))
