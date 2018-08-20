from user_operation.serializers import usermsgserializer
from rest_framework.response import Response
from user_operation.models import UserLeavingMessage
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import status


class usermsgviews(generics.ListAPIView):
    # def get(self, request, format=None):
    #     usermodel = UserLeavingMessage.objects.all()[:10]
    #     usermsg_serializer = usermsgserializer(usermodel, many=True)
    #     return Response(usermsg_serializer.data)
    queryset = UserLeavingMessage.objects.all()[:10]
    serializer_class = usermsgserializer
