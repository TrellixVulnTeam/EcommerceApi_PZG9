from rest_framework import serializers
from . models import Product

              
    
class ProductSerializer(serializers.ModelSerializer):
                   
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'created_at','size','brand']
        
        
        

  