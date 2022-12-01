from django.utils.translation import gettext as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class UserAdmin(UserAdmin):
   #добавляем отображение кастомных полей в админке
   fieldsets = (
    (None, {'fields': ('username', 'password')}),
    (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
    (_('Permissions'), {
        'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
    }),
    (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    (_('Additional Info'), {'fields': ('userpic', 'theme', 'description', 'userslug')}),
   )

admin.site.register(MyUser, UserAdmin)

class articlesAdmin(admin.ModelAdmin):
   # отображаемые поля
   list_display = ('id', 'section', 'title', 'subtitle', 'author', 'time_create', 'content', 'is_published')
   # кликабельность поля
   list_display_links = ('id', 'title')
   # по каким поляем работает поиск
   search_fields = ['title', 'subtitle', 'text'] 

admin.site.register(articles, articlesAdmin)

class commentsAdmin(admin.ModelAdmin):
   model = comments
   list_display = ('post', 'author', 'text', 'time_create', 'is_active')
   list_display_links = ('post', 'author')
   search_fields = ['post', 'author', 'text']

admin.site.register(comments, commentsAdmin)

class likesAdmin(admin.ModelAdmin):
   model = likes
   list_display = ('post', 'liked_by', 'time_create')
   
admin.site.register(likes, likesAdmin)