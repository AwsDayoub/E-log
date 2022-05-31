from distutils.command.upload import upload
from operator import mod
from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import get_user_model
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'categories'


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey('Post',on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.username
    

class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='',null=True,blank=True)
    image_url = models.CharField(max_length=200,default=None,null=True,blank=True)
    date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    published = models.BooleanField()

    def __str__(self):
        return self.title