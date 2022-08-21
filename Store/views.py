from webbrowser import get
from django.shortcuts import render, get_object_or_404
from Store import serializers
from Store.serializers import ProductSerializer
from . models import *
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics, mixins

from rest_framework.views import APIView

# Create your views here.


#Retreiving all products and creates a product      
class ProductsListView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
    def get(self, request: Request, *args, **kwargs):
            return self.list(request, *args, **kwargs)


    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


#Retreiving, Updating and Deleteing a post
class ProductDetailView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


    
    



    

    
    
    
    