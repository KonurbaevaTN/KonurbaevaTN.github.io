"""
Definition of models.
"""

from email.policy import default
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
from datetime import datetime
from django.contrib import admin 
from django.urls import reverse
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(unique_for_date="posted", max_length= 100, verbose_name="Заголовок")
    description = models.TextField(verbose_name = "Краткое содержание")
    content = models.TextField(verbose_name = "Полное содержание")
    posted = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Опубликована")

    image = models.FileField(default = 'book.jpg', verbose_name="C:/Users/Татьяна/Downloads/DjangoWebProject1/DjangoWebProject1/DjangoWebProject1/media/book.jpg")

    def get_absolute_url(self):
        return reverse("blogpost", args=[str(self.id)])


    def __str__(self):
        return self.title

    class Meta:
        db_table = "Post"
        ordering = ['-posted']
        verbose_name = "статья блога"
        verbose_name_plural = "статьи блога"


admin.site.register(Blog)


class Comment(models.Model):
    text = models.TextField(verbose_name = "Комментарий")
    date = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Дата")
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Автор")
    post = models.ForeignKey(Blog, on_delete = models.CASCADE, verbose_name = "Статья")

    def __str__(self):
        return 'Комментарий %s к %s' % (self.author, self.post)

    class Meta:
        db_table = "Comments"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии к статьям блога"
        ordering = ["-date"]


admin.site.register(Comment)