from django.db import models
from django.contrib.auth.models import User

#хранение контента
class articles(models.Model):
   section = models.CharField(max_length=15)
   title = models.CharField(max_length=100)
   slug = models.SlugField(max_length=1001)
   subtitle = models.CharField(max_length=50)
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   avatar = models.ImageField(height_field=None, width_field=None) # ?
   text = models.TextField(blank=True)
   content = models.FileField(height_field=None, width_field=None, upload_to='files/%Y/%m/%d')
   time_create = models.DateTimeField(auto_now_add=True)
   is_published = models.BooleanField(default=True)
   
class comments(models.Model):
   article_title = models.ForeignKey(articles, on_delete=models.CASCADE)
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   time_create = models.DateTimeField(auto_now_add=True)
   text = models.TextField()
   