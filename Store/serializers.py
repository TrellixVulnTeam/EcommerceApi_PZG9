from rest_framework import serializers
from . models import Product
from drf_writable_nested.serializers import WritableNestedModelSerializer

              
    
class ProductSerializer(serializers.ModelSerializer):
                   
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'created_at','size','brand']
        
        
        

  