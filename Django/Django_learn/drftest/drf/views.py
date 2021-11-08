import re
import uuid

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import exceptions, status, serializers
from rest_framework.versioning import QueryParameterVersioning, URLPathVersioning, AcceptHeaderVersioning, HostNameVersioning, NamespaceVersioning
from rest_framework.exceptions import AuthenticationFailed   # 认证失败返回
from rest_framework.authentication import BaseAuthentication   # 继承的基础认证类
from rest_framework.permissions import BasePermission
from rest_framework.filters import BaseFilterBackend
from rest_framework.throttling import SimpleRateThrottle
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.mixins import ListModelMixin, DestroyModelMixin, UpdateModelMixin, RetrieveModelMixin, CreateModelMixin
from django.core.cache import cache as default_cache
from django.core.validators import EmailValidator
from django.forms.models import model_to_dict
from django_filters.rest_framework import DjangoFilterBackend

from drf import models



# ############v0测试版本工具
# Create your views here.
# class UserView(APIView):
#     # versioning_class = QueryParameterVersioning  # get 传递
#     # versioning_class = URLPathVersioning    # url传递
#     versioning_class = AcceptHeaderVersioning     # 请求头传递
#     def get(self, request, *args, **kwargs):
#         print(request.version)
#         return Response({'code': 200, 'data': '111'})
#
#     def post(self, request, *args, **kwargs):
#         return Response({'code': 300, 'data': '222'})





class AuthView(APIView):
    """ 用户登录认证 """
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        print(request.data)  # {"username": "wupeiqi", "password": "123"}
        username = request.data.get('username')
        password = request.data.get('password')

        user_object = models.UserInfo.objects.filter(username=username, password=password).first()
        if not user_object:
            return Response({"code": 1000, "data": "用户名或密码错误"})

        token = str(uuid.uuid4())  # 生成随机的token

        user_object.token = token
        user_object.save()

        return Response({"code": 0, "data": {"token": token, "name": username}})


class TokenAuthentication(BaseAuthentication):
    '''认证'''
    def authenticate(self, request):
        token = request.query_params.get("token")
        if not token:
            raise AuthenticationFailed({"code": 1002, "data": "认证失败"})
        user_object = models.UserInfo.objects.filter(token=token).first()
        if not user_object:
            raise AuthenticationFailed({"code": 1002, "data": "认证失败"})
        return user_object, token

    def authenticate_header(self, request):
        return 'Bearer realm="API"'


class PermissionA(BasePermission):
    '''权限'''
    message = {"code": 1003, 'data': "无权访问"}   # 无权访问的时候返回的信息

    def has_permission(self, request, view):
        if request.user.role == 2:
            return True
        return False

    # 判断用户对obj对象的访问权限
    def has_object_permission(self, request, view, obj):
        return True

class Filter1(BaseFilterBackend):
    '''自定义过滤器'''
    def filter_queryset(self, request, queryset, view):
        age = request.query_params.get('age')
        if not age:
            return queryset
        return queryset.filter(age=age)


class ThrottledException(exceptions.APIException):
    status_code = status.HTTP_429_TOO_MANY_REQUESTS
    default_code = 'throttled'


class MyRateThrottle(SimpleRateThrottle):
    cache = default_cache  # 访问记录存放在django的缓存中（需设置缓存）
    scope = "user"  # 构造缓存中的key
    cache_format = 'throttle_%(scope)s_%(ident)s'

    # 设置访问频率，例如：1分钟允许访问10次
    # 其他：'s', 'sec', 'm', 'min', 'h', 'hour', 'd', 'day'
    THROTTLE_RATES = {"user": "10/m"}

    def get_cache_key(self, request, view):
        if request.user:
            ident = request.user.pk  # 用户ID
        else:
            ident = self.get_ident(request)  # 获取用户IP
        return self.cache_format % {'scope': self.scope, 'ident': ident}

    def throttle_failure(self):
        wait = self.wait()
        detail = {
            "code": 1005,
            "data": "访问频率限制",
            'detail': "需等待{}s才能访问".format(int(wait))
        }
        raise ThrottledException(detail)

class OrderView(APIView):
    throttle_classes = [MyRateThrottle, ]

    def get(self, request):
        return Response({"code": 0, "data": "数据..."})

    def throttled(self, request, wait):
        detail = {
            "code": 1005,
            "data": "访问频率",
            'detail': "需等待{}s才能访问".format(int(wait))
        }
        raise ThrottledException(detail)


class RegexValidator(object):
    def __init__(self, base):
        self.base = str(base)

    def __call__(self, value):
        match_object = re.match(self.base, value)
        if not match_object:
            raise serializers.ValidationError('格式出错')




# ####################v1测试第一种数据校验
# class UserSerializer(serializers.Serializer):
#     '''验证方式1'''
#     username = serializers.CharField(label='姓名', min_length=6, max_length=32)
#     age = serializers.CharField(label='年龄', min_length=0, max_length=200)
#     # level = serializers.CharField(label='级别', choices=models.UserInfo.role)
#     email = serializers.CharField(label='邮箱', validators=[EmailValidator, ])
#     email1 = serializers.CharField(label='邮箱1')
#     email2 = serializers.CharField(label='邮箱2', validators=[RegexValidator(r'^\w+@\w+\.\w+$'), ])
#     email3 = serializers.CharField(label='邮箱3')
#
#     def validated_email3(self, value):
#         '''钩子函数，验证email3'''
#         if re.match(r'^\w+@\w+\.\w+$'):
#             return value
#         raise exceptions.ValidationError('邮箱格式错误')
#





# ####################v1测试第二种数据校验
class UserModelSerializer(serializers.ModelSerializer):
    '''验证方式2'''
    email2 = serializers.CharField(label='邮箱2', validators=[RegexValidator(r'^\w+@\w+\.\w+$'), ])
    email3 = serializers.CharField(label='邮箱3')

    class Meta:
        model = models.UserInfo
        fields = ['username', 'age', 'email', 'depart', 'roles', 'email2', 'email3']
        extra_kwargs = {
            'username': {'min_length': 6, 'max_length': 32},
            'email': {'validators': [EmailValidator, ]}
        }

    def validated_email3(self, value):
        '''钩子函数，验证email3'''
        if re.match(r'^\w+@\w+\.\w+$'):
            return value
        raise exceptions.ValidationError('邮箱格式错误')

class UserView(APIView):
    def post(self, request):  # 此request为drf再次封装后的
        print(request.data)
        ser = UserModelSerializer(data=request.data)
        if not ser.is_valid():
            return Response({'code': 1006, 'data': ser.errors})

        print(ser.validated_data)

        ser.validated_data.pop('email2')
        ser.validated_data.pop('email3')  # 剔除数据库中未创建的两个字段
        ser.save(level=1, password='123', depart_id=1)  # 带的参数为未输入的字段的给定默认值
        return Response({'code': 200, 'data': '创建成功'})





# 数据序列化展示
#####v1
class UserModelSerializer1(serializers.ModelSerializer):
    class Meta:
        model = models.UserInfo
        # fields = '__all__' 一次性展示所有的字段
        fields = ['username', 'age', 'email', 'depart', 'roles']


        extra_kwargs = {
            'username': {'min_length': 6, 'max_length': 32},
            'email': {'validators': [EmailValidator, ]}
        }

####v2序列化展示，增加中文显示，以及自定义和增加字段
class UserModelSerializer2(serializers.ModelSerializer):
    level_text = serializers.CharField(source='get_level_display')
    depart = serializers.CharField(source='depart.title')

    # 自定义显示格式，分别在下面各自定义方法
    roles = serializers.SerializerMethodField()
    extra = serializers.SerializerMethodField()

    class Meta:
        model = models.UserInfo
        fields = ['username', 'age', 'email', 'level_text', 'depart', 'roles', 'extra']

    def get_roles(self, obj):
        data_list = obj.roles.all()
        return [model_to_dict(item, ['id', 'title']) for item in data_list]

    def get_extra(self, obj):
        return 666

class UserGet(APIView):
    '''用户查询数据'''
    def get(self, request):
        queryset = models.UserInfo.objects.all()
        # ser = UserModelSerializer1(instance=queryset, many=True)
        ser = UserModelSerializer2(instance=queryset, many=True)

        print(ser.data)
        return Response({'code': 201, 'data': '查询成功'})


# 五大视图测试
class UserViewSite(ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin, RetrieveModelMixin, GenericViewSet):
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['age', 'depart']

    queryset = models.UserInfo.objects.all()
    # serializer_class = UserModelSerializer2   # 直接定义序列化方法

    # 通过判断定义序列化方法
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserModelSerializer2
        return UserModelSerializer1



