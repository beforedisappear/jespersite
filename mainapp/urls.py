from django.urls import path

from .views import *

#name - имя страницы (неявный url адрес)
urlpatterns = [
    path('', index, name='home'),
    path('economy/', economy, name='economy'),
    path('develoment', dev, name='develoment'),
    path('life', life, name='life'),
]
