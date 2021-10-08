from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import QueryParameterVersioning

# Create your views here.

class UserView(APIView):
    # versioning_class = QueryParameterVersioning

    def get(self, request, *args, **kwargs):
        print(request.version)
        return Response({"code": 1000, "data": "xxx"})

    def post(self, request, *args, **kwargs):
        return Response({"code": 1000, "data": "xxx"})
