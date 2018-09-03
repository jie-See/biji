# -*-coding:utf-8-*-

from rest_framework import serializers
from goods.models import Goods, GoodsImage
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


class GoodsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        fields = ("image",)


class GoodsSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    images = GoodsImageSerializer(many=True)

    class Meta:
        model = Goods
        fields = '__all__'


class GoodsCategoryBrandserializers(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategoryBrand
        fields = '__all__'


class CategorySerializer3(serializers.ModelSerializer):
    '''三级分类'''
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True)
    '''二级分类'''
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    '''一级类别序列化'''
    sub_cat = CategorySerializer2(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"

