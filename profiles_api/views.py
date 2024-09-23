from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
# Create your views here.
class HelloApiView(APIView):
    serializers_class=serializers.HelloSerializer
    def get(self,request, format=None):

        an_apiview=[
            "first api view"
        ]

        return Response({"message":"hello" , "an_apiview":an_apiview})
    def post(self,request):
        serializer=self.serializers_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        return Response({'method':"put"})

    def patch(self, request, pk=None):
        return Response({'method': "patch"})

    def delete(self, request, pk=None):
        return Response({'method': "delete"})

class HelloViewSet(viewsets.ViewSet):

    serializer_class=serializers.HelloSerializer
    def list(self,request):
        a_viewset=[
            "uses actions list create retrive"
        ]
        return Response({"message":a_viewset})

    def create(self,request):

        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrive(self,request,pk=None):
        return Response({'http_method':"get"})