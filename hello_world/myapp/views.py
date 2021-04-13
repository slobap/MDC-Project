from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django_filters import rest_framework as filters
from .models import Task, Tag
from .serializers import TaskSerializer, TagSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets

class TaskViewSet(viewsets.ModelViewSet):

    def list(self, request):
        task_list = Task.objects.all()
        serializer_class = TaskSerializer(task_list, many=True)
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None):
        task = Task.objects.all()
        task_retrieve = get_object_or_404(self.task, pk=pk)
        serializer_task = TaskSerializer(task_retrieve)
        return Response(serializer_task.data)
  
class TagViewSet(viewsets.ModelViewSet):
    
    def list(self, request):   
        tag_list = Tag.objects.all()  
        serializer_class = TagSerializer(tag_list, many=True)
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None):
        tag = Tag.objects.all()
        tag_retrieve = get_object_or_404(self.tag, pk=pk)
        serializer_tag = TagSerializer(tag_retrieve)
        return Response(serializer_tag.data)

    