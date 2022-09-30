from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

menu = ['Экономика', 'Кино', 'Игры', 'Разработка / IT', 'Поиск', 'Войти']

def index(request):
    return render(request, 'mainapp/index.html', {'menu': menu, 'title': 'Главная страница'})

def about(request):
    return HttpResponse('<h1>О сайте</h1>')

#обработка исключения при несовпадении шаблона
def PageNotFound (request, exception):
    return HttpResponseNotFound('<h>Страница не найдена</h>')