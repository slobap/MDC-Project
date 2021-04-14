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
        queryset = Task.objects.all()
        serializer_class = TaskSerializer(queryset, many=True)
        Response(serializer_class.data)

class TagViewSet(viewsets.ModelViewSet):   
        queryset = Tag.objects.all()  
        serializer_class = TagSerializer(queryset, many=True)
        Response(serializer_class.data)

    