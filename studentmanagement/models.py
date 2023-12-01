from django.db import models
# Create your models here.
class Student(models.Model):
    name = models.CharField(default='',max_length=255)
    hobby = models.CharField(default='',max_length=255)
