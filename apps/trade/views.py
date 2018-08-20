from django.shortcuts import render
from .serializers import orderserializer
from .models import OrderInfo
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class orderview(APIView):
    def get(self, request, format = None):
        order = OrderInfo.objects.all()[:10]
        order_serializer = orderserializer(order, many=True)
        return Response(order_serializer.data)