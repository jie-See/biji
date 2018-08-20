import datetime

from django.contrib.auth.backends import ModelBackend
from django.shortcuts import render
from .serializers import UserRegSerializer
from rest_framework.views import APIView
from .models import UserProfile
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.db.models import Q
# Create your views here.
User = get_user_model()


# class Userprofile(APIView):
#     def get(self, request, format = None):
#         user = UserProfile.objects.all()[:10]
#         user_serializer = userserializer(user, many=True)
#         return Response(user_serializer.data)


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username)|Q(mobile=username))
            if user.check_password(password):
                return user

        except Exception as e:
            return None


from rest_framework.mixins import CreateModelMixin
from rest_framework import viewsets
from .serializers import SmsSerializer
from rest_framework.response import Response
from rest_framework import status
from utils.yunpian import YunPian
from biji.settings import APIKEY
from random import choice
from .models import VerifyCode


class SmsCodeViewset(CreateModelMixin,viewsets.GenericViewSet):
    '''
    手机验证码
    '''
    serializer_class = SmsSerializer

    def generate_code(self):
        """
        生成四位数字的验证码
        """
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))

        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        #验证合法
        serializer.is_valid(raise_exception=True)

        mobile = serializer.validated_data["mobile"]

        yun_pian = YunPian(APIKEY)
        #生成验证码
        code = self.generate_code()

        sms_status = yun_pian.send_sms(code=code, mobile=mobile)

        if sms_status["code"] != 0:
            return Response({
                "mobile": sms_status["msg"]
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = VerifyCode(code=code, mobile=mobile)
            code_record.save()
            return Response({
                "mobile": mobile
            }, status=status.HTTP_201_CREATED)


class UserViewset(CreateModelMixin,viewsets.GenericViewSet):
    '''
    用户
    '''
    serializer_class = UserRegSerializer
