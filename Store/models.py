from operator import truediv
from django.db import models
from django.contrib.auth.models import User

#Create your models here


# size choices for product
class SizeChoices(models.TextChoices):    
    
    EXTRA_SMALL = 'XS'
    SMALL = "S"
    MEDIUM = "M"
    LARGE = "L"
    EXTRA_LARGE = 'XL'

class BrandChoices(models.TextChoices):
    
    NIKE = 'Nike'
    DIOR = 'Dior'
    ADIDAS = 'Adidas'
    UNDER_ARMOUR = 'Under Armour'
    H_and_M = 'H&M'
    ZARA = 'Zara'
    POLO = 'Polo'
    LEVIS = 'Levis'       
    


#Customer model - OneToOne with User 
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    
    
    def __str__(self):
        return self.name

       
#Product model - OneToMany with OrderItem   
class Product(models.Model):
    
    name = models.CharField(max_length=50, null=False, blank=False)
    price = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    brand = models.CharField(max_length=20, choices=BrandChoices.choices, default=BrandChoices.DIOR)
    size = models.CharField(max_length=20, choices=SizeChoices.choices, default=SizeChoices.EXTRA_SMALL)

    
    class Meta:
        ordering = ['-created_at']
        
        
    def __str__(self):
        return self.name
    
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, related_name='products', null=True)
    date_of_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return "Customer - {} Transaction ID - {} ".format(self.customer.name, str(self.transaction_id))
    
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name='products', null=truediv)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
    
    
    
class ShippingCustomerAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=50,null=True)
    zipcode = models.CharField(max_length=100,null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.customer.email
