
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from register.views import *

router = routers.SimpleRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),

]
