from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Task/', views.TaskViewSet.as_view('list')),
    path('Tag/', views.TagViewSet.as_view('list')),
    path('api-auth/', include('rest_framework.urls'))
]