from django.urls import path
from django.shortcuts import redirect
from . import views
from django.views.generic.base import RedirectView
from . import friend_request

urlpatterns = [
path('',RedirectView.as_view(url='home')),
path('home/', views.home, name='home'),
path('home/register', views.register, name='register'),
path('home/login', views.loginpage, name='login'),
path('logout', views.logoutuser, name='logoutuser'),
path('shome/send_request/<int:id>/', friend_request.send_friend_request, name='send_frequest'),
path('shome/cancel_request/<int:id>/', friend_request.cancel_friend_request, name='cancel_frequest'),
path('thome/accept_request/<int:id>/', friend_request.accept_friend_request, name='accept_frequest'),
path('thome/delete_request/<int:id>/', friend_request.delete_friend_request, name='delete_frequest'),

]