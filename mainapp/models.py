from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

#хранение контента
class articles(models.Model):
   SECTIONS = [('Economy', 'Экономика'), ('Dev/IT', 'Разработка | IT'), ('Life', 'Жизнь')]
   section = models.CharField(max_length=15, choices=SECTIONS)
   title = models.CharField(max_length=100, verbose_name='Заголовок')
   slug = models.SlugField(max_length=1001, unique=True, db_index=True, verbose_name='URL')
   subtitle = models.CharField(max_length=50, verbose_name='Подзаголовок', blank=True)
   #встроенная модель пользователя
   author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
   text = models.TextField(blank=True, verbose_name='Текст')
   content = models.FileField(upload_to='files/%Y/%m/%d')
   time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
   is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
   
   #формирование маршрута к конкретной записи
   def get_absolute_url(self):
       return reverse("post", kwargs={"post_id": self.pk})
    
   #вложенный класс для настройки админ панели
   class Meta:
      verbose_name = 'Статьи'
      verbose_name_plural = 'Статьи'
      #сортировка отображения статей
      ordering = ['time_create']
   
   
class comments(models.Model):
   article_title = models.ForeignKey(articles, on_delete=models.CASCADE, 
                                     related_name='coms',verbose_name='Статья')
   author = models.ForeignKey(User, on_delete=models.CASCADE,
                              verbose_name='Автор комментария')
   text = models.TextField(verbose_name='Текст комментария')
   time_create = models.DateTimeField(auto_now_add=True)
   is_active = models.BooleanField(default=True, verbose_name='Опубликовано')
   

class сomment_answer(models.Model):
   comment = models.ForeignKey(comments, on_delete=models.CASCADE)
   author = models.ForeignKey(User, on_delete=models.CASCADE,
                              verbose_name='Автор комментария')
   text = models.TextField(verbose_name='Текст комментария')
   time_create = models.DateTimeField(auto_now_add=True)
   is_active = models.BooleanField(default=True, verbose_name='Опубликовано') 
   
class likes(models.Model):
   pass