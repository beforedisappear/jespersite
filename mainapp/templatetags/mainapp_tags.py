import os
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
   return articles.objects.filter(is_published=True, section='economy').order_by('-time_create')


@register.simple_tag(name='getdev')
def get_economy():
   return articles.objects.filter(is_published=True, section='dev').order_by('-time_create')


@register.simple_tag(name='getlife')
def get_economy():
   return articles.objects.filter(is_published=True, section='life').order_by('-time_create')
