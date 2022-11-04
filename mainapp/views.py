from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseNotFound
from django.views.generic import ListView, DetailView

from .forms import *
from .models import *


# основная страница
class HomePage(ListView):
    model = articles # ссылка на модель (отображение записей в виде list)
    template_name = 'mainapp/index.html' # путь к оторажаемому шаблону
    context_object_name = 'posts' # переменная для хранения коллекции записей
    extra_context = {'title': 'Главная страница'}
    
    # метод отбора записей из БД
    def get_queryset(self):
        return articles.objects.filter(is_published=True).order_by('-time_create')
    

def economy(request):
    return render(request, 'mainapp/economy.html', {'title': 'Экономика'})


def dev(request):
    return render(request, 'mainapp/dev.html', {'title': 'Разработка | IT'})


def life(request):
    return render(request, 'mainapp/life.html', {'title': 'Жизнь'})


# def show_article(request, post_slug):
#     # находим статью в БД по slug
#     article = get_object_or_404(articles, slug=post_slug)
#     context = {
#         'post': article,
#         'title': article.title,
#     }
#     return render(request, 'mainapp/article.html', context=context)

# отображение статьи на её странице
class ShowArtice(DetailView):
    model = articles
    template_name = 'mainapp/article.html' 
    slug_url_kwarg = 'post_slug' #своя переменная для слага
    context_object_name = 'post'
        

# функция представления персональной страницы юзера
def personal_page(request):
    # сохранение введеных данных в случае их невалидности
    if request.method == 'POST':
        form = AddArticleForm(request.POST, request.FILES)
        if form.is_valid():
            # добавление новой записи в БД
            form.save()
            return redirect('home')
    else:
        form = AddArticleForm()
    list_articles = articles.objects.order_by('-time_create')
    list_users = User
    context = {
        'post': list_articles,
        'users': list_users,
        'title': 'personal-page'
    }
    return render(request, 'mainapp/p.html', context)


# обработка исключения при несовпадении шаблона
def PageNotFound(request, exception):
    return HttpResponseNotFound('<h>Страница не найдена</h>')
