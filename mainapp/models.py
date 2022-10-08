from email.policy import default
from django.db import models

#хранение контента
class articles(models.Model):
   section = models.CharField(max_length=15)
   title = models.CharField(max_length=100)
   slug = models.SlugField(max_length=1001)
   subtitle = models.CharField(max_length=50)
   creator = models.CharField(max_length=20)
   avatar = models.ImageField(height_field=None, width_field=None)
   content = models.TextField() #filefield?
   photo = models.ImageField(height_field=None, width_field=None, upload_to='photos/%Y/%m/%d')
   time_create = models.DateTimeField(auto_now_add=True)
   is_published = models.BooleanField(default=True)
   #com = models.ManyToManyField('comments', null=True) #fix connection
   
class comments(models.Model):
   nickname = models.CharField(max_length=20, db_index=True)
   time_create = models.DateTimeField(auto_now_add=True)
   cmnt = models.TextField()
   