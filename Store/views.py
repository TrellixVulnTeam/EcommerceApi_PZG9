from distutils.command.install_egg_info import safe_name
from itertools import product
from webbrowser import get
from django.shortcuts import render, get_object_or_404
from Store import serializers
from Store.serializers import ProductSerializer
from . models import *
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework import generics, mixins
from rest_framework.views import APIView

# Create your views here.

@api_view(['GET','POST'])
def hello_mac(request):
    
    if request.method == 'POST':
        post_data = request.data
        response = {
            'message' : 'created',
            'data': post_data
        }

        return Response(data=response)
    
    elif request.method == 'GET':    
        return Response({'message': 'Hello Mac'})
    

class ProductsCustom(APIView):
    
    
    
    def get(self, request : Request):
        
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
    
        response = {
            'message' : 'created',
            'count' : queryset.count(),
            'data': serializer.data
 
        }
        
        return Response(data=response, status= status.HTTP_200_OK)
    
    
    def post(self, request: Request):
        
        
        serializer = ProductSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            response = {
            'message' : 'product created!',
            'data': serializer.data
 
        }
            return Response(data=response, status= status.HTTP_201_CREATED)

class ProductCustomDetails(APIView):
    
    def put(self, request : Request, product_id):
        
        product = get_object_or_404(Product, pk=product_id)

        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            response = {
            'message' : 'product created!',
            'data': serializer.data
 
        }      
            return Response(data=serializer.data, status = status.HTTP_200_OK)
    
        return Response(data={'message': 'product not found!'}, status = status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, product_id, format=None):
        product = get_object_or_404(Product, pk=product_id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Retreiving all products and creates a product      
class ProductsListView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get(self, request: Request, *args, **kwargs):
            return self.list(request, *args, **kwargs)


    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


#Retreiving, Updating and Delete a post
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


    
    



    

    
    
    
    