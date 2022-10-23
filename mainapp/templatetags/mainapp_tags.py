from atexit import register
from django import template
from mainapp.models import *

#хранение логики работы тегов

#экземпляр класс Library, через который происходит
#создание собственных шаблонных тегов
register = template.Library()


#простой тег, возвращающий из БД все записи таблицы article
@register.simple_tag(name='getarticles')
def get_articles():
   return articles.objects.all()


@register.simple_tag(name='geteconomy')
def get_economy():
   return articles.objects.filter(section='economy')


@register.simple_tag(name='getdev')
def get_economy():
   return articles.objects.filter(section='dev')

@register.simple_tag(name='getlife')
def get_economy():
   return articles.objects.filter(section='life')