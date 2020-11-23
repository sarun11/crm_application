from django.db import models
# Create your models here
from customer.models import Customer


class Tag(models.Model):
    name = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    
    CATEGORY = (
        ('Stationery', 'Stationery'),
        ('Sports Items', 'Sports'),
        ('Clothing', 'Clothing'),
        ('Miscellaneous', 'Misc')
    )
    
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=30, null=True, choices=CATEGORY) 
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
    

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for Delivery', 'OUT for Delivery'),
        ('Delivered', 'Delivered')
    )

    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=25, null=True, choices=STATUS)
     
    def __str__(self):
        return str(self.customer) + "_" + str(self.product)
