from django.db.migrations import serializer
from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins

from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from register.models import *
from register.premissions import IsOwnerOrAdmin
from register.serializers import *


# Create your views here.

class UserAPIList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class UserAPICheckSelf(generics.RetrieveUpdateAPIView):     Получение и изменение Газа для
#     queryset = Gas.objects.all()                            Определенного пользователя
#     serializer_class = ContentSerializer


class UserAPICheckSelf(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsOwnerOrAdmin , )

    # def perform_create(self, serializer):
    #     serializer.save(data=self.request.user)

class UserAPIDelete(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)



class UserAPIDataUpdate(APIView):
    serializer_class = DataSerializer
    model = Data
    # permission_classes = (IsOwnerOrAdmin,)

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        try:
            instance = Data.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})
        serializer = DataSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})



# class UserAPIDataUpdate(generics.RetrieveUpdateAPIView,
#                         mixins.ListModelMixin,
#                         mixins.CreateModelMixin,) :
#     queryset = Data.objects.all()
#     serializer_class = DataSerializer
#     permission_classes = (IsOwnerOrAdmin, )
#     def post(self, request, username):
#         if request.method == 'POST':
#             data = get_object_or_404(Data, pk=username)
#             print("Request ====" , request.data)
#             data = DataSerializer(request)
#             data = JSONParser().parse(request)
#             serializer = DataSerializer(data=data)
#             print(serializer)
#             return Response({'Data type' : "hz"})














@receiver(pre_save, sender = User)
def createData(instance, **kwargs) :
    user = instance
    if User.objects.filter(username=user.username).exists():
        return
    else:
        Gas.objects.create(userID = user.username)
        Water.objects.create(userID=user.username)
        Electricity.objects.create(userID=user.username)
        Data.objects.create(userID=user.username, gas_id = user.username, water_id = user.username, electricity_id = user.username)
        user.data_id = user.username


