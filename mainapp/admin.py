from django.contrib import admin
from .models import *

class articlesAdmin(admin.ModelAdmin):
   # отображаемые поля
   list_display = ('id', 'section', 'title', 'subtitle', 'author', 'time_create', 'content', 'is_published')
   # кликабельность поля
   list_display_links = ('id', 'title')
   # по каким поляем работает поиск
   search_fields = ('title', 'subtitle', 'author', 'text')
   # автоматическое формирование слага
   #prepopulated_fields = {'slug': ('title',)} # добавить pk !

admin.site.register(articles, articlesAdmin)