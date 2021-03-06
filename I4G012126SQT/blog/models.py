from cgitb import text
from turtle import title
from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default='')
    created_date = models.DateTimeField()
    published_date = models.DateTimeField()
