from django.conf.urls import url
from . import views
from views import *

urlpatterns = [
    url('', views.get, name='get'),
    path('api-auth/', include('rest_framework.urls'))
    path('api-token-auth/', views.obtain_auth_token)
    url('advanced_filters/', include('advanced_filters.urls'))
]