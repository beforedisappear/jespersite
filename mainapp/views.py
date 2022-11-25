from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.urls import reverse_lazy
from .forms import *
from .models import *


# основная страница
class HomePage(ListView):
    template_name = 'mainapp/index.html'                # путь к оторажаемому шаблону
    context_object_name = 'posts'                       # переменная для хранения коллекции записей

    # метод отбора записей из БД
    def get_queryset(self):
        return articles.objects.filter(is_published=True).order_by('-time_create')
    
    # формирование контекста страницы
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)    #получаем сформированный контекст
        context['title'] = 'Главная страница'
        return context
        
class economy(ListView):
    template_name = 'mainapp/economy.html'
    context_object_name = 'posts'
    extra_context = {'title': 'Экономика'}
    
    # отбор записей в раздел экономика
    def get_queryset(self):
        return articles.objects.filter(is_published=True, section='economy').order_by('-time_create')
    
class dev(ListView):
    template_name = 'mainapp/dev.html'
    context_object_name = 'posts'
    extra_context = {'title': 'Разработка | IT'}
    
    # отбор записей в раздел экономика
    def get_queryset(self):
        return articles.objects.filter(is_published=True, section='dev').order_by('-time_create')
    
class life(ListView):
    template_name = 'mainapp/dev.html'
    context_object_name = 'posts'
    extra_context = {'title': 'Жизнь'}
    
    # отбор записей в раздел экономика
    def get_queryset(self):
        return articles.objects.filter(is_published=True, section='life').order_by('-time_create')


# отображение статьи на её странице
class ShowArtice(DetailView):
    model = articles
    template_name = 'mainapp/article.html'
    slug_url_kwarg = 'post_slug'  # своя переменная для слага
    context_object_name = 'post'  # html
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)    #получаем сформированный контекст
        context['title'] = self.object.title
        return context


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
    list_articles = articles.objects.filter(is_published=True).order_by('-time_create')
    context = {
        'post': list_articles,
        'title': 'personal-page'
    }
    return render(request, 'mainapp/p.html', context)

class AdminLogin(LoginView):
    form_class = AuthenticationForm                  # форма авторизации пользователя 
    template_name = 'mainapp/adminlogin.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)    #получаем сформированный контекст
        context['title'] = 'Авторизация'
        return context
    
    def get_success_url(self):
        return reverse_lazy('home')
    
class userpage(DetailView):
    model = MyUser
    template_name = 'mainapp/p.html'
    slug_url_kwarg = 'username'
    slug_field = 'userslug'

    # def get(self, request, username):
    #     user = get_object_or_404(MyUser, username=username)
    #     return render(request, 'mainapp/p.html', {'thisuser': user, 'title': 'JESPER — ' + user.first_name})
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)    #получаем сформированный контекст
        user = get_object_or_404(MyUser, userslug=self.kwargs['username'])
        context['thisuser'] = user
        context['title'] = 'JESPER — ' + user.first_name
        return context
    

class userpagesettings(DetailView):
    model = MyUser
    template_name = 'mainapp/psettings.html'
    slug_url_kwarg = 'username'
    slug_field = 'userslug'
    
    # def get(self, request, username):
    #     user = get_object_or_404(MyUser, username=username)
    #     return render(request, 'mainapp/psettings.html', {'thisuser': user, 'title': 'Настройки '})
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)    #получаем сформированный контекст
        user = get_object_or_404(MyUser, userslug=self.kwargs['username'])
        context['thisuser'] = user
        context['title'] = 'Настройки пользователя'
        return context

    

# обработка исключения при несовпадении шаблона
def PageNotFound(request, exception):
    return render(request, 'mainapp/error.html')

# выход
def logout_user(request):
    logout(request)
    return redirect('/')
