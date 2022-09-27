from logging import exception
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def index(request):
    return HttpResponse('Hello')

def about(request):
    return HttpResponse('<h1>О сайте</h1>')

#обработка исключения при несовпадении шаблона
def PageNotFound (request, exception):
    return HttpResponseNotFound('<h>Страница не найдена</h>')

    