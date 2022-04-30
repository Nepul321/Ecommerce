from django.db import models
from base.models import User
from orders.models import (
    Order
)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=255)
    order = models.OneToOneField(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    zipcode = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.address)
