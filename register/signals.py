from django.db.models.signals import pre_save
from django.dispatch import receiver

from register.models import *


# @receiver(pre_save, sender = User)
# def createData(instance, **kwargs) :
#     user = instance
#     if User.objects.filter(username=user.email).exists():
#         return
#     else:
#         Gas.objects.create(userID = user.username)
#         Water.objects.create(userID=user.username)
#         Electricity.objects.create(userID=user.username)
#         Data.objects.create(userID=user.username, gas_id = user.username, water_id = user.username, electricity_id = user.username)
#         user.data_id = user.username

