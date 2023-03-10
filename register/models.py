from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class Gas(models.Model) :
    oneAgo = models.IntegerField(null=True, blank = True)
    twoAgo = models.IntegerField(null=True, blank = True)
    thirdAgo = models.IntegerField(null=True, blank = True)
    fourAgo = models.IntegerField(null=True, blank = True)
    fiveAgo = models.IntegerField(null=True, blank = True)
    sixAgo = models.IntegerField(null=True, blank = True)
    sevenAgo = models.IntegerField(null=True, blank = True)
    eightAgo = models.IntegerField(null=True, blank = True)
    nineAgo = models.IntegerField(null=True, blank = True)
    tenAgo = models.IntegerField(null=True, blank = True)
    elevenAgo = models.IntegerField(null=True, blank = True)
    twelveAgo = models.IntegerField(null=True, blank = True)
    userID = models.CharField(primary_key=True, max_length=30)

    def __str__(self):
        return self.userID


class Water(models.Model) :
    oneAgo = models.IntegerField(null=True, blank=True)
    twoAgo = models.IntegerField(null=True, blank=True)
    thirdAgo = models.IntegerField(null=True, blank=True)
    fourAgo = models.IntegerField(null=True, blank=True)
    fiveAgo = models.IntegerField(null=True, blank=True)
    sixAgo = models.IntegerField(null=True, blank=True)
    sevenAgo = models.IntegerField(null=True, blank=True)
    eightAgo = models.IntegerField(null=True, blank=True)
    nineAgo = models.IntegerField(null=True, blank=True)
    tenAgo = models.IntegerField(null=True, blank=True)
    elevenAgo = models.IntegerField(null=True, blank=True)
    twelveAgo = models.IntegerField(null=True, blank=True)
    userID = models.CharField(primary_key=True, max_length=30)

    def __str__(self):
        return self.userID

class Electricity(models.Model) :
    oneAgo = models.IntegerField(null=True, blank=True)
    twoAgo = models.IntegerField(null=True, blank=True)
    thirdAgo = models.IntegerField(null=True, blank=True)
    fourAgo = models.IntegerField(null=True, blank=True)
    fiveAgo = models.IntegerField(null=True, blank=True)
    sixAgo = models.IntegerField(null=True, blank=True)
    sevenAgo = models.IntegerField(null=True, blank=True)
    eightAgo = models.IntegerField(null=True, blank=True)
    nineAgo = models.IntegerField(null=True, blank=True)
    tenAgo = models.IntegerField(null=True, blank=True)
    elevenAgo = models.IntegerField(null=True, blank=True)
    twelveAgo = models.IntegerField(null=True, blank=True)
    userID = models.CharField(primary_key=True, max_length=30)

    def __str__(self):
        return self.userID



class Data(models.Model):
    GasActual = models.IntegerField(null=True, blank=True)
    GasOneAgo = models.IntegerField(null=True, blank=True)
    WaterActual = models.IntegerField(null=True, blank=True)
    WaterOneAgo = models.IntegerField(null=True, blank=True)
    ElectricityActual = models.IntegerField(null=True, blank=True)
    ElectricityOneAgo = models.IntegerField(null=True, blank=True)
    userID = models.CharField(primary_key=True, max_length=30)
    gas = models.OneToOneField(Gas, on_delete=models.CASCADE, null=True, blank=True)
    water = models.OneToOneField(Water, on_delete=models.CASCADE, null=True, blank=True)
    electricity = models.OneToOneField(Electricity, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.userID



class User(AbstractUser) :
    licSchet = models.CharField(max_length=20, unique=True)
    username = models.EmailField('email' ,unique=True, primary_key=True)
    data = models.OneToOneField(Data, on_delete=models.CASCADE, null=True, blank=True)

    REQUIRED_FIELDS = ['licSchet', 'password', 'data']


    def __str__(self):
        return self.username





