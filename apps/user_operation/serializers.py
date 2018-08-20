from rest_framework import serializers
from user_operation.models import UserLeavingMessage


class usermsgserializer(serializers.ModelSerializer):
    class Meta:
        model = UserLeavingMessage
        field = "__all__"
