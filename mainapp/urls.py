from django.urls import path, include

from django.conf.urls import *

from .views import *

#name - имя страницы (неявный url адрес)
#as_view() - вызов ф. связи класса с маршрутом
urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('economy/', economy, name='economy'),
    path('dev/', dev, name='dev'),
    path('life/', life, name='life'),
    path('article/<slug:post_slug>/', ShowArtice.as_view(), name='article'),
    path('logout/', logout_user, name='logout'),
    path('p/', personal_page, name='personal-page'),
    
    path('social-auth/', include('social_django.urls', namespace='social')),
]
#'social.apps.django_app.urls'