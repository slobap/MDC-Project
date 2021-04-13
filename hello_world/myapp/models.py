from django.db import models
import django_filters

class Task(models.Model):
    project_title = models.CharField(max_length=100)
    tags = models.ManyToManyField('Tag', through='All')
    subject = models.CharField(max_length=100)
    project_id = models.IntegerField()

class Tag(models.Model):
    word = models.CharField(max_length=100)
    tasks = models.ManyToManyField('Task', through='All')

class All(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
