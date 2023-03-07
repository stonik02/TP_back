from django.forms import model_to_dict
from rest_framework import generics, viewsets

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from register.models import *
from register.serializers import UserSerializer


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



# class UserAPIView(generics.ListAPIView) :
#     queryset = User.objects.all()
#     serializer_class = UserSerializer



# class UserAPIList(generics.ListCreateAPIView):
#     queryset =  User.objects.all()
#     serializer_class = UserSerializer
#
#
#
# class UserAPIUpdate(generics.UpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserAPIView(APIView) :
#     def get(self, request):
#         lst = User.objecsts.all().values()
#         return Response({'posts' : list(lst)})
#
#     def post(self, request):
#         user_new = User.objects.create(
#             ""
#         )                                              # В двух строчках проверяем
#                                                              # вверно ли введены данные в POST
#
#         serializer.save()
#
#         return Response({'post' : serializer.data})



