"""Определяет схемы URL для пользователей"""
from django.urls import path, include
from . import views


app_name = 'users'

urlpatterns = [
    # Include the default authentication urls
    path('', include('django.contrib.auth.urls')),
    # Вывод всех тем.
    path('users/logout/', views.logout_view, name='logout'),
    #Реристрация пользователя
    path('users/register/', views.register, name='register'),
]