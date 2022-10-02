from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

menu = ['Экономика', 'Разработка | IT', 'Жизнь', 'Поиск', 'Войти']


def index(request):
    return render(request, 'mainapp/index.html', {'menu': menu, 'title': 'Главная страница'})

def economy(request):
    return HttpResponse('<h1>Экономика</h1>')

def dev(request):
    return HttpResponse('<h1>Разработка и IT</h1>')

def life(request):
    return HttpResponse('<h1>life</h1>')

#обработка исключения при несовпадении шаблона
def PageNotFound (request, exception):
    return HttpResponseNotFound('<h>Страница не найдена</h>')