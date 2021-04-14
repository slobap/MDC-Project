from django.db import models
import django_filters

class Task(models.Model):
    project_title = models.CharField(max_length=100)
    tags = models.ManyToManyField('Tag', through='Tag')
    subject = models.CharField(max_length=100)
    project_id = models.IntegerField()

class Tag(models.Model):
    word = models.CharField(max_length=100)
    tag_id = models.IntegerField()