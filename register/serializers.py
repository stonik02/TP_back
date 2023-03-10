from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from register.models import *




class GasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gas
        fields = '__all__'

class WaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Water
        fields = '__all__'

class ElectricitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Electricity
        fields = '__all__'



class DataSerializer(serializers.ModelSerializer):
    # GasActual = serializers.IntegerField()
    # GasOneAgo = serializers.IntegerField()
    # WaterActual = serializers.IntegerField()
    # WaterOneAgo = serializers.IntegerField()
    # ElectricityActual = serializers.IntegerField()
    # ElectricityOneAgo = serializers.IntegerField()
    gas = GasSerializer(many=False, read_only=True)
    water = WaterSerializer(many=False, read_only=True)
    electricity = ElectricitySerializer(many=False, read_only=True)

    class Meta:
        model = Data
        fields = ("GasActual", "GasOneAgo", "WaterActual",
                  "WaterOneAgo", "ElectricityActual",
                  "ElectricityOneAgo",
                  "gas", "water", "electricity"
                  )
        depth = 1

    def update(self, instance, validated_data):

        if validated_data.get("GasActual") != None :

            instance.GasOneAgo = validated_data.get("GasOneAgo", instance.GasActual)
            instance.GasActual = validated_data.get("GasActual", instance.GasActual)

            one = instance.gas.oneAgo
            two = instance.gas.twoAgo
            third = instance.gas.thirdAgo
            four = instance.gas.fourAgo
            five = instance.gas.fiveAgo
            six = instance.gas.sixAgo
            seven = instance.gas.sevenAgo
            eight = instance.gas.eightAgo
            nine = instance.gas.nineAgo
            ten = instance.gas.tenAgo
            eleven = instance.gas.elevenAgo

            instance.gas.oneAgo = instance.GasOneAgo
            instance.gas.twoAgo = one
            instance.gas.thirdAgo = two
            instance.gas.fourAgo = third
            instance.gas.fiveAgo = four
            instance.gas.sixAgo = five
            instance.gas.sevenAgo = six
            instance.gas.eightAgo = seven
            instance.gas.nineAgo = eight
            instance.gas.tenAgo = nine
            instance.gas.elevenAgo = ten
            instance.gas.twelveAgo = eleven

            instance.gas.save()

        if validated_data.get("WaterActual") != None:

            instance.WaterOneAgo = validated_data.get("WaterOneAgo", instance.WaterActual)
            instance.WaterActual = validated_data.get("WaterActual", instance.WaterActual)

            one = instance.water.oneAgo
            two = instance.water.twoAgo
            third = instance.water.thirdAgo
            four = instance.water.fourAgo
            five = instance.water.fiveAgo
            six = instance.water.sixAgo
            seven = instance.water.sevenAgo
            eight = instance.water.eightAgo
            nine = instance.water.nineAgo
            ten = instance.water.tenAgo
            eleven = instance.water.elevenAgo

            instance.water.oneAgo = instance.WaterOneAgo
            instance.water.twoAgo = one
            instance.water.thirdAgo = two
            instance.water.fourAgo = third
            instance.water.fiveAgo = four
            instance.water.sixAgo = five
            instance.water.sevenAgo = six
            instance.water.eightAgo = seven
            instance.water.nineAgo = eight
            instance.water.tenAgo = nine
            instance.water.elevenAgo = ten
            instance.water.twelveAgo = eleven

            instance.water.save()

        if validated_data.get("ElectricityActual") != None:

            instance.ElectricityOneAgo = validated_data.get("ElectricityOneAgo", instance.ElectricityActual)
            instance.ElectricityActual = validated_data.get("ElectricityActual", instance.ElectricityActual)

            one = instance.electricity.oneAgo
            two = instance.electricity.twoAgo
            third = instance.electricity.thirdAgo
            four = instance.electricity.fourAgo
            five = instance.electricity.fiveAgo
            six = instance.electricity.sixAgo
            seven = instance.electricity.sevenAgo
            eight = instance.electricity.eightAgo
            nine = instance.electricity.nineAgo
            ten = instance.electricity.tenAgo
            eleven = instance.electricity.elevenAgo

            instance.electricity.oneAgo = instance.ElectricityOneAgo
            instance.electricity.twoAgo = one
            instance.electricity.thirdAgo = two
            instance.electricity.fourAgo = third
            instance.electricity.fiveAgo = four
            instance.electricity.sixAgo = five
            instance.electricity.sevenAgo = six
            instance.electricity.eightAgo = seven
            instance.electricity.nineAgo = eight
            instance.electricity.tenAgo = nine
            instance.electricity.elevenAgo = ten
            instance.electricity.twelveAgo = eleven

            instance.electricity.save()

        instance.save()
        return instance







class UserSerializer(serializers.ModelSerializer):

    data = DataSerializer(many=False, read_only=True)
    class Meta:
        model = User
        fields = ("username", "password", "licSchet",  "data")
        depth = 2

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gas
        fields = ("pk", )









