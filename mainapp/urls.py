from django.urls import path

from .views import *

#name - имя страницы (неявный url адрес)
#as_view() - вызов ф. связи класса с маршрутом
urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('economy/', economy, name='economy'),
    path('dev/', dev, name='dev'),
    path('life/', life, name='life'),
    path('article/<slug:post_slug>/', ShowArtice.as_view(), name='article'),
    path('p/', personal_page, name='personal-page'),
]
