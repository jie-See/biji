from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from user_operation.models import UserFav
from user_operation.models import UserLeavingMessage


class usermsgserializer(serializers.ModelSerializer):
    class Meta:
        model = UserLeavingMessage
        field = "__all__"


class UserFavSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                message='已经收藏'
            )
        ]
        model = UserFav
        fields = ('user', 'goods', 'id')
