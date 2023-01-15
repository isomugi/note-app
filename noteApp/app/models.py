from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.
#使うモデルの名前や変数等を設定する　
#https://itc.tokyo/django/all-about-modelfield/ モデルフィールドについて
class Author(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    create = models.DateTimeField(auto_now_add=True)
    saved = models.DateTimeField(auto_now=True)

class Note(models.Model):
    #title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(verbose_name='内容')
    image = models.FileField(
        upload_to = 'uploads/%yY/%m/%d',
        validators = [FileExtensionValidator(['png','jpg','jpeg'])]
    )
    url = models.URLField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

