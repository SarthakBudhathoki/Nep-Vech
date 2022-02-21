from email import message
from django.db import models

# Create your models here.

class Product(models.Model):
    product_id=models.AutoField(auto_created=True,primary_key=True)
    product_name=models.CharField(max_length=200)
    product_detail=models.CharField(max_length=1000)
    product_price=models.IntegerField()
    product_image=models.FileField(upload_to='product')

    class Meta:
        db_table="product"

class Contact(models.Model):
    contact_id=models.AutoField(auto_created=True,primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=1000)

    class Meta:
        db_table="contact"