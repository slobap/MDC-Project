from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django_filters import rest_framework as filters
import django_filters.rest_framework
from .models import Task, Tag
from .serializers import TaskSerializer, TagSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, filters

class TaskViewSet(viewsets.ModelViewSet, generics.ListAPIView):
        queryset = Task.objects.all()
        serializer_class = TaskSerializer(queryset, many=True)
        filter_backends = [filters.SearchFilter, filters.OrderingFilter]
        search_fields = '__all__'
        ordering_fields = '__all__'
        ordering = ['project_title']
        Response(serializer_class.data)

class TagViewSet(viewsets.ModelViewSet):   
        queryset = Tag.objects.all()  
        serializer_class = TagSerializer(queryset, many=True)
        filter_backends = [filters.SearchFilter, filters.OrderingFilter]
        search_fields = '__all__'
        ordering_fields = '__all__'
        ordering = ['word']
        Response(serializer_class.data)

    