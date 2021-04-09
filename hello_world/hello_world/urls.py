from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from myapp import views
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/Task/', views.taskList.as_view()),
    path('api/Tag/', views.tagList.as_view()),
]