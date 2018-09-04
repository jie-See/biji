import datetime

from django.contrib.auth.backends import ModelBackend
from django.shortcuts import render
<<<<<<< HEAD
from rest_framework_jwt.serializers import jwt_payload_handler
from rest_framework_jwt.utils import jwt_encode_handler

from .serializers import UserRegSerializer, UserDtailSerializer
=======
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from .serializers import UserRegSerializer
>>>>>>> 8b17a8a663d07dac8e010e0e23a3dafee2791da1
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


from rest_framework import mixins, permissions
from rest_framework import viewsets
from .serializers import SmsSerializer, UserDtailSerializer
from rest_framework.response import Response
from rest_framework import status
from utils.yunpian import YunPian
from biji.settings import APIKEY
from random import choice
from .models import VerifyCode
from rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication



class SmsCodeViewset(mixins.CreateModelMixin,viewsets.GenericViewSet):
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


class UserViewset(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    用户
    '''
    serializer_class = UserRegSerializer
    queryset = User.objects.all()
<<<<<<< HEAD
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
=======
>>>>>>> 8b17a8a663d07dac8e010e0e23a3dafee2791da1

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["name"] = user.name if user.name else user.username

        headers = self.get_success_headers(serializer.data)

        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

<<<<<<< HEAD
    # 这里需要动态权限配置
    # 1.用户注册的时候不应该有权限限制
    # 2.当想获取用户详情信息的时候，必须登录才行
    def get_permissions(self):
        if self.action == "retrieve":
            return [permissions.IsAuthenticated()]
        elif self.action == "create":
            return []

        return []

    # 这里需要动态选择用哪个序列化方式
    # 1.UserRegSerializer（用户注册），只返回username和mobile，会员中心页面需要显示更多字段，所以要创建一个UserDetailSerializer
    # 2.问题又来了，如果注册的使用userdetailSerializer，又会导致验证失败，所以需要动态的使用serializer
    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDtailSerializer
        elif self.action == "create":
            return UserRegSerializer

        return UserDtailSerializer

    # 虽然继承了Retrieve可以获取用户详情，但是并不知道用户的id，所有要重写get_object方法
    # 重写get_object方法，就知道是哪个用户了
    def get_object(self):
        return self.request.user

=======
>>>>>>> 8b17a8a663d07dac8e010e0e23a3dafee2791da1
    def perform_create(self, serializer):
        return serializer.save()



<<<<<<< HEAD

=======
>>>>>>> 8b17a8a663d07dac8e010e0e23a3dafee2791da1
