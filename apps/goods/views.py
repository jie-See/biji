from django.shortcuts import render
from .serializers import GoodsSerializers, GoodsCategoryBrandserializers, CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Goods, GoodsCategory
from rest_framework import mixins
from rest_framework import generics
from goods.models import GoodsCategoryBrand
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .filters import GoodsFilter
# Create your views here.


class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class GoodsListViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Goods.objects.all().order_by('id')
    serializer_class = GoodsSerializers
    pagination_class = GoodsPagination

    # filter_backends = (DjangoFilterBackend,)
    # filter_fields = ('name', 'shop_price')
    # filter_backends = (DjangoFilterBackend,)
    # filter_class = GoodsFilter

    # def post(self, request, format=None):
    #     serializer = GoodsSerializers(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class GoodsCategoryBrandView(APIView):
    def get(self,request, format=None):
        brand = GoodsCategoryBrand.objects.all()[0:10]
        brand_serializer = GoodsCategoryBrandserializers(brand, many=True)
        return Response(brand_serializer.data)


class CategoryViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    '''
    list:
        商品分类列表数据
    '''
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer
