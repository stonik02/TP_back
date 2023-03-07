from django.contrib.auth.models import AbstractUser
from django.db import models


class Gas(models.Model) :
    actual = models.IntegerField(null=True, blank = True)
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
    licSchet = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.licSchet


class Water(models.Model) :
    actual = models.IntegerField(null=True, blank=True)
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
    licSchet = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.licSchet

class Electricity(models.Model) :
    actual = models.IntegerField(null=True, blank=True)
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
    licSchet = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.licSchet



class User(AbstractUser) :
    licSchet = models.CharField(max_length=20, unique=True)
    username = models.CharField('Логин', max_length=30, blank=True, unique=True)
    gas = models.OneToOneField(Gas, on_delete=models.PROTECT, null=True, blank=True)
    water = models.OneToOneField(Water, on_delete=models.PROTECT, null=True, blank=True)
    electricity = models.OneToOneField(Electricity, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.username
