from rest_framework import serializers
from .models import OrderInfo





class orderserializer(serializers.ModelSerializer):
    class Meta:
        model = OrderInfo
        fields = "__all__"