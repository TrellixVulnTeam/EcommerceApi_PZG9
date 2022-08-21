from django.contrib import admin
from . models import Product, Customer, Order, OrderItem, ShippingCustomerAddress


# Register your models here.
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(ShippingCustomerAddress)