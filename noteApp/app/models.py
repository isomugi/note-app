from django.db import models

# Create your models here.
class Auther(models.Model):
    name = models.CharField(max_length=20)
    create = models.DateTimeField(auto_now_add=True)
    saved = models.DateTimeField(auto_now=True)

class Note(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=200)
