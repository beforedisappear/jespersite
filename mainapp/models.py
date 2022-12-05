from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.core.validators import FileExtensionValidator

from uuslug import uuslug, slugify

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/users/user_<username>/<filename>
    return 'users/user_{0}/{1}'.format(instance.username, filename)

#расширяем встроенную модель User
class MyUser(AbstractUser):
   id = models.AutoField(primary_key=True)
   userslug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name='UserSlug')
   userpic = models.ImageField(upload_to=user_directory_path, blank=True, verbose_name='Аватар', default='baseuserpic.jpg' )
   theme = models.ImageField(upload_to=user_directory_path, blank=True, verbose_name='Фон')
   description = models.CharField(max_length=150, blank=True, verbose_name='Пару слов о себе')
   
   def save(self, *args, **kwargs):
      if not self.first_name:                                                             #базовый ник = login
         self.first_name = self.username
      if self.is_superuser:                                                               #slug for superuser                                      
         self.userslug = self.username.lower().replace(' ', '-')
      super(MyUser, self).save(*args, **kwargs)
      self.update_user_slug() 
      
   def update_user_slug(self):
      # You now have both access to self.id
      if not self.is_superuser: 
         #now have both access to self.id
         self.userslug = str(self.id) + '-' + slugify(self.first_name.lower().replace(' ', '-')) #slug for user
         MyUser.objects.filter(id=self.id).update(userslug=self.userslug)



from uuslug import uuslug, slugify


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/users/user_<username>/<filename>
    return 'users/user_{0}/{1}'.format(instance.username, filename)

#расширяем встроенную модель User
class MyUser(AbstractUser):
   id = models.AutoField(primary_key=True)
   userslug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name='UserSlug')
   userpic = models.ImageField(upload_to=user_directory_path, blank=True, verbose_name='Аватар', default='baseuserpic.jpg' )
   theme = models.ImageField(upload_to=user_directory_path, blank=True, verbose_name='Фон')
   description = models.CharField(max_length=150, blank=True, verbose_name='Пару слов о себе')
   
   def save(self, *args, **kwargs):
      if not self.first_name:                                                             #базовый ник = login
         self.first_name = self.username
      if self.is_superuser:                                                               #slug for superuser                                      
         self.userslug = self.username.lower().replace(' ', '-')
      super(MyUser, self).save(*args, **kwargs)
      self.update_user_slug() 
      
   def update_user_slug(self):
      # You now have both access to self.id
      if not self.is_superuser: 
         #now have both access to self.id
         self.userslug = str(self.id) + '-' + slugify(self.first_name.lower().replace(' ', '-')) #slug for user
         MyUser.objects.filter(id=self.id).update(userslug=self.userslug)


#хранение контента
class articles(models.Model):
   SECTIONS = [('economy', 'Экономика'), ('dev', 'Разработка | IT'), ('life', 'Жизнь')]
   section = models.CharField(max_length=15, choices=SECTIONS)
   title = models.CharField(max_length=150, verbose_name='Заголовок')
   slug = models.SlugField(max_length=1001, unique=True, db_index=True, verbose_name='URL')
   subtitle = models.CharField(max_length=350, verbose_name='Подзаголовок', blank=True)
   #many articles to one user
   author = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='Автор')
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
      
   #тип файла
   def get_file_type(self):
      a = self.content.name.find('.')+1
      if self.content.name[a:] in ['jpg', 'png', 'heic']: return 'photo'
      elif self.content.name[a:] in  ['mp4', 'mov', 'heic']: return 'video'
   
   #метод для отображения объекта
   def __str__(self):
      return self.title
   
   #вложенный класс для настройки админ панели
   class Meta:
      verbose_name = 'Статьи'
      verbose_name_plural = 'Статьи'
      #сортировка отображения статей
      ordering = ['time_create']
   
   
class comments(models.Model):
   # через cmnts можем обратиться к множеству объектов класса comments, связанных с объектом класса articles
   post = models.ForeignKey(articles, on_delete=models.CASCADE, related_name='cmnts', verbose_name='Статья')
   author = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, verbose_name='Автор комментария')
   text = models.TextField(verbose_name='Текст комментария')
   time_create = models.DateTimeField(auto_now_add=True)
   is_active = models.BooleanField(default=True, verbose_name='Опубликовано')
   
   class Meta:
      verbose_name = 'Комментарии'
      verbose_name_plural = 'Комментарии'
      ordering = ['time_create']
   
   
class сomment_answer(models.Model):
   comment = models.ForeignKey(comments, on_delete=models.CASCADE)
   author = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING,
                              verbose_name='Автор комментария')
   text = models.TextField(verbose_name='Текст комментария')
   time_create = models.DateTimeField(auto_now_add=True)
   is_active = models.BooleanField(default=True, verbose_name='Опубликовано') 
   
class likes(models.Model):
   #many likes to one article
   post = models.ForeignKey(articles, on_delete=models.CASCADE, related_name='lks', verbose_name='Статья')
   like = models.BooleanField(default=False, verbose_name='Лайки')
   liked_by = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, verbose_name='Автор лайка')
   time_create = models.DateTimeField(auto_now_add=True)
   
   class Meta:
      verbose_name = 'Лайки'
      verbose_name_plural = 'Лайки'
      ordering = ['time_create']