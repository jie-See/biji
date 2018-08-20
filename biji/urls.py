"""biji URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
from rest_framework.authtoken import views

from biji.settings import MEDIA_ROOT
from django.views.static import serve
from goods.views import GoodsListViewset,GoodsCategoryBrandView
from rest_framework.documentation import include_docs_urls
from trade.views import orderview
# from user.views import Userprofile
from user_operation.views import usermsgviews
import xadmin
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from user.views import SmsCodeViewset,UserViewset

router = DefaultRouter()


# goods_list = GoodsListView.as_view({
#
#     'get': 'list',
#
# }
# )

router.register(r'goods', GoodsListViewset)
router.register(r'code', SmsCodeViewset, base_name="code")
router.register(r'users', UserViewset, base_name="users")

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    url(r'^', include(router.urls)),
    url(r'^login', obtain_jwt_token),
    # url(r'^api-token-auth/', views.obtain_auth_token)
    # url(r'^docs/', include_docs_urls(title="生鲜")),
    # url(r'^trade/', orderview.as_view(), name="order_list"),
    # url(r'^user/', Userprofile.as_view(), name="user"),
    # url(r'^useroperation/', usermsgviews.as_view(), name="userfav"),
    # url(r'^goodsbrand/', GoodsCategoryBrandView.as_view(),name="goodsbrand")
]
