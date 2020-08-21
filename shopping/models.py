from django.db import models
from catalogue.models import Product
from customers.models import Customer
from shippinng.models import ShippingProvider


# Create your models here.
from django.contrib.auth.models import User
class Cart(models.Model):
    products = models.OneToOneField(Product, on_delete=models.CASCADE)
    date_created = models.DateTimeField()
    
    def __str__(self):
        return self.products()




class Order(models.Model):
    order_number = models.IntegerField()
    date_placed = models.DateTimeField()
    status = models.CharField(max_length=28)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    #payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    delivery_time = models.DateTimeField()
    shipping_provider =models.ForeignKey(ShippingProvider, on_delete=models.CASCADE)
    order_price = models.DecimalField(max_digits=10, decimal_places=3)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
       
    def __str__(self):
          return self.order

class Payment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=28)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_payment = models.DateTimeField()

    def __str__(self):
        return self.customer