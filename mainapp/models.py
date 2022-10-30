from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import FileExtensionValidator

from uuslug import uuslug




#хранение контента
class articles(models.Model):
   SECTIONS = [('economy', 'Экономика'), ('dev', 'Разработка | IT'), ('life', 'Жизнь')]
   section = models.CharField(max_length=15, choices=SECTIONS)
   title = models.CharField(max_length=150, verbose_name='Заголовок')
   slug = models.SlugField(max_length=1001, unique=True, db_index=True, verbose_name='URL')
   subtitle = models.CharField(max_length=350, verbose_name='Подзаголовок', blank=True)
   #встроенная модель пользователя
   author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
   text = models.TextField(blank=True, verbose_name='Текст')
   time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
   is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
   content = models.FileField(upload_to='files/%Y/%m/%d', blank=True, validators=[
      FileExtensionValidator(
         allowed_extensions=['jpg', 'png', 'mp4', 'gif', 'mov', 'heic'], 
         message='Некорректный формат файла!',
         )
      ])
   
   #формирование маршрута к конкретной записи
   def get_absolute_url(self):
      # 'article' - имя маршрута в urls.py
      return reverse("article", kwargs={"post_slug": self.slug})
   
   def __unicode__(self):
      return self.title

   #транслитерация слага
   def save(self, *args, **kwargs):
      self.slug = uuslug(self.title, instance=self)
      super(articles, self).save(*args, **kwargs) 
      
   def get_file_type(self):
      a = self.content.name.find('.')+1
      if self.content.name[a:] in ['jpg', 'png', 'heic']: return 'photo'
      elif self.content.name[a:] in  ['mp4', 'mov', 'heic']: return 'video'
   
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