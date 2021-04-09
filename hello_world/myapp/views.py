from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Task, Tag
from rest_framework import viewsets, permissions, status, filters
from myapp.serializers import TaskSerializer, TagSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from django.views import generic
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters

class taskList(APIView):

    def get(self, request):
        task1 = Task.objects.all()       
        serializer1 = TaskSerializer(task1, many=True)               
        return Response(serializer1.data)  

    def post(self):
        pass

class tagList(APIView):
    def get(self, request):
        tag1 = Tag.objects.all()
        serializer2 = TagSerializer(tag1, many=True)
        return Response(serializer2.data)

    def post(self):
        pass

class TaskListView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = '__all__'
    search_fields = '__all__'

class TagListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = '__all__'
    search_fields = '__all__'