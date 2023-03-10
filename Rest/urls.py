
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

from djoser.views import *

from register.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/rest-auth/' , include('rest_framework.urls')),
    path('api/v1/user/', UserAPIList.as_view()),
    path('api/v1/user/<pk>/', UserAPICheckSelf.as_view()),
    path('api/v1/userdelete/<pk>/', UserAPIDelete.as_view()),
    path('api/v1/user/data/<pk>/', UserAPIDataUpdate.as_view()),




    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

]
