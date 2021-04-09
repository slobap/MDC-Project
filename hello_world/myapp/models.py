from django.db import models
import django_filters

class Task(models.Model):
    project = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    project_id = models.IntegerField()

class Tag(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    word = models.CharField(max_length=100)
    

    def __str__(self):
        return str(self.task)
        return str(self.tag)