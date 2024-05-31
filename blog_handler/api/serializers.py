from rest_framework import serializers
from .models import Catagory
from django.contrib.auth.models import User


class CatagorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Catagory
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'