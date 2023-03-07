from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from register.models import *



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","email", "username", "licSchet", "gas", "water", "electricity")



# class UserSerializer (serializers.Serializer) :
#     licSchet = serializers.CharField(max_length=20)
#     email = serializers.EmailField()
#     username = serializers.CharField( max_length=30)
#     password = serializers.CharField(max_length=30)
#
#     def create(self, validated_data):
#         return User.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.email = validated_data.get("email", instance.email)
#         instance.password = validated_data.get("password", instance.password)
#         instance.licSchet = validated_data.get("licSchet", instance.licSchet)
#         instance.save()
#         return instance





