from django.contrib import admin
from .models import Task, Tag, All

admin.site.register(Task)
admin.site.register(Tag)
admin.site.register(All)