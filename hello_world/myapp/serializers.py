from rest_framework import serializers
from myapp.models import Task, Tag

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['project', 'subject', 'created_at']

class TagSerializer(serializers.ModelSerializer):
    class Tag:
        model = Tag
        fields = ['task', 'word']