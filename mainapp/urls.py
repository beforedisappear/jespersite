from django.urls import path

from .views import *

#name - имя страницы (неявный url адрес)
urlpatterns = [
    path('', index, name='home'),
    path('economy/', economy, name='economy'),
    path('dev/', dev, name='dev'),
    path('life/', life, name='life'),
    path('article/<slug:post_slug>/', show_article, name='article')
]
