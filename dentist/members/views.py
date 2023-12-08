# from django.shortcuts import render
# from django.views import generic
# from django.views.generic import CreateView
# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
# from web.models import Topbar, NavbarHeading
#
# # Create your views here.
#
#
# class UserRegisterView(CreateView):
#     form_class = UserCreationForm
#     template_name = 'register.html'
#     success_url = reverse_lazy('login')
#
#
# class LoginView(CreateView):
#     form_class = UserCreationForm
#     template_name = 'login.html'
#     success_url = reverse_lazy('home')
#     top = Topbar.objects.all()
#     navbar = NavbarHeading.objects.all()
#     context = {'top': top, 'navbar': navbar, }