# -*-coding:utf-8-*-

from rest_framework import serializers
from goods.models import Goods
from goods.models import GoodsCategory
from goods.models import GoodsCategoryBrand


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = '__all__'#('name', 'click_num', 'market_price', 'add_time')
    # name = serializers.CharField(required=True,max_length=100)
    # click_num = serializers.IntegerField(default=0)

    # def create(self, validated_data):
        # return Goods.objects.create(**validated_data)


class GoodsSerializers(serializers.ModelSerializer):
    category = CategorySerializers()

    class Meta:
        model = Goods
        fields = '__all__'


class GoodsCategoryBrandserializers(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategoryBrand
        fields = '__all__'
