from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.
class customUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=20)


class Blog(models.Model):
    title = models.CharField(max_length=100)
    short_desc = models.CharField(max_length=250)
    desc = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='media/')
    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(customUser,on_delete=models.CASCADE)