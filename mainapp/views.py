from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseNotFound
from .models import *

menu = ['Экономика', 'Разработка | IT', 'Жизнь']


def index(request):
    list_articles = articles.objects.all()
    context = {
        'posts': list_articles,
        'menu': menu,
        'title': 'Главная страница',
    }
    return render(request, 'mainapp/index.html', context=context)

def economy(request):
    return render(request, 'mainapp/economy.html', {'menu': menu, 'title': 'Экономика'})

def dev(request):
    return render(request, 'mainapp/dev.html', {'menu': menu, 'title': 'Разработка | IT'})

def life(request):
    return render(request, 'mainapp/life.html', {'menu': menu, 'title': 'Жизнь'})

def show_article(request, post_slug):
    #находим статью в БД по slug
    article = get_object_or_404(articles, slug=post_slug)
    context = {
        'post': article,
        'menu': menu,
        'title': article.title,
    }
    return render(request, 'mainapp/article.html', context=context)

#обработка исключения при несовпадении шаблона
def PageNotFound (request, exception):
    return HttpResponseNotFound('<h>Страница не найдена</h>')