from unittest.util import _MAX_LENGTH
from django.db import models

class articles(models.Model):
   title = models.CharField(max_length=100)
   creator = models.CharField(max_lenght=20)
   subtitle = models.CharField(max_length=50)
   content = models.TextField()
   photo = models.ImageField()
   section = models.TextField()
   time_create = models.DateTimeField(auto_now_add=True)
   is_published = models.BooleanField()
   
class comments(models.Model):
   pass