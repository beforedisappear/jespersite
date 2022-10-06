from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

menu = ['Экономика', 'Разработка | IT', 'Жизнь']


def index(request):
    return render(request, 'mainapp/index.html', {'menu': menu, 'title': 'Главная страница'})

def economy(request):
    return render(request, 'mainapp/economy.html', {'menu': menu, 'title': 'Экономика'})

def dev(request):
    return render(request, 'mainapp/dev.html', {'menu': menu, 'title': 'Разработка | IT'})

def life(request):
    return render(request, 'mainapp/life.html', {'menu': menu, 'title': 'Жизнь'})

#обработка исключения при несовпадении шаблона
def PageNotFound (request, exception):
    return HttpResponseNotFound('<h>Страница не найдена</h>')