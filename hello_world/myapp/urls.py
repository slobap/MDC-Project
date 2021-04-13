from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from myapp.views import TaskViewSet, TagViewSet

router = DefaultRouter
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'tags', TagViewSet, basename='tag')
urlpatterns = router.urls

urlpatterns = [
    url('/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    url('advanced_filters/', include('advanced_filters.urls'))
]