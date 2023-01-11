from django.db import models

# Create your models here.
class Auther(models.Model):
    name = models.CharField(max_length=20)

class Note(models.Model):
    date = models.DateTimeField
    content = models.CharField(max_length=200)
