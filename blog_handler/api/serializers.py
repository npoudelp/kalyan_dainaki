from rest_framework import serializers
from .models import Catagory

class CatagorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Catagory
        fields = '__all__'