from django.db import models

class articles(models.Model):
   title = models.CharField(max_length=100)
   subtitle = models.CharField(max_length=50)
   creator = models.CharField(max_length=20)
   content = models.TextField()
   photo = models.ImageField()
   section = models.TextField()
   time_create = models.DateTimeField(auto_now_add=True)
   is_published = models.BooleanField()
   
class comments(models.Model):
   pass