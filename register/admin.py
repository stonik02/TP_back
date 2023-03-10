from django.contrib import admin

import register
from register.models import *

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['pk','licSchet', 'username', 'data_id', 'is_superuser']



@admin.register(Gas)
class GasAdmin(admin.ModelAdmin) :
    list_display = ['pk','oneAgo', 'userID']
    list_editable = []

@admin.register(Water)
class WaterAdmin(admin.ModelAdmin) :
    list_display = ['pk','oneAgo', 'userID']
    list_editable = []

@admin.register(Electricity)
class ElectricityAdmin(admin.ModelAdmin):
    list_display = ['pk','oneAgo', 'userID']
    list_editable = []

@admin.register(Data)
class Data(admin.ModelAdmin):
    list_display = ['userID','GasActual', 'GasOneAgo', 'WaterActual',
                    'WaterOneAgo', 'ElectricityActual', 'ElectricityOneAgo',
                    'gas', 'water', 'electricity',
                    ]