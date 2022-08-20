from operator import truediv
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


#Customer model - OneToOne with User 
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    
    
    def __str__(self):
        return self.name
    
#Brand model - OneToOne with Product
class Brand(models.Model):
    name = models.CharField(max_length=20, null=False)

   
    def __str__(self):
        return self.name


   
#Product model - OneToMany with OrderItem   
class Product(models.Model):
    
    sizeChoices = (
        ('s','Small'),
        ('m', 'Medium'),
        ('l', 'Large'),
        ('xl','Extra Large')
    )
     
    name = models.CharField(max_length=50, null=False, blank=False)
    price = models.FloatField(blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    brand = models.OneToOneField(Brand, on_delete=models.CASCADE)   
    size = models.CharField(max_length=20, choices=sizeChoices)


    def __str__(self):
        return self.name
    
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, related_name='products', null=True)
    date_of_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        #set the name of the customer here as well in the order
        return " Customer - {} Transaction ID - {}".format(self.customer.name, str(self.transaction_id))
    
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name='products', null=truediv)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.product.name

class ShippingCustomerAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=50,null=True)
    zipcode = models.CharField(max_length=100,null=True)
    date_added = models.DateTimeField(auto_now_add=True)



    

