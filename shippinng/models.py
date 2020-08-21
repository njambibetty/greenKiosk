from django.db import models
from shopping.models import Order
from shippinng.models import ShippingProvider

# Create your models here.

from django.contrib.auth.models import User
class Name(models.Model):

    name = models.CharField(max_length=28)
    date_joined = models.CharField(max_length=28)
    email = models.EmailField()
    phone_number = models.IntegerField()
    transport_mode = models.CharField(max_length=28)


    def __str__(self):
        return self.name
    


class DispenserCoolerBox(models.Model):
    box_number = models.IntegerField()
    location = models.CharField()
    unlock_code = models.IntegerField()

    def __str__(self):
        return self.box_number

class Order(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    dispatch_time = models.DateTimeField()
    shipping_provider= models.ForeignKey(ShippingProvider, on_delete=models.CASCADE)
    cooler_box = models.ForeignKey(Coolerbox, on_delete=models.CASCADE)


    def __str__(self):
        return self.order



  
      

