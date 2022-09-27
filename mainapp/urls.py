from django.contrib import admin
from django.urls import path, include

from .views import *

#name - имя страницы (неявный url адрес)
urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about')
]
