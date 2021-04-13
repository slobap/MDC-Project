from rest_framework import serializers
from myapp.models import Task, Tag, All

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class AllSerializer(serializers.ModelSerializer):
    class Meta:
        model = All
        fields = '__all__'