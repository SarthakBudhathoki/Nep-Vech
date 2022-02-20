from django.db import models
from django.contrib.auth import get_user_model

from home.models import Product

# Create your models here.

class Booking(models.Model):
    booking_id=models.AutoField(auto_created=True,primary_key=True)
    customer=models.CharField(max_length=200)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    price=models.IntegerField()

    class Meta:
        db_table="booking"

