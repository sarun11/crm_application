from django.db import models

# Create your models here

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=30, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Order(models.Model):
    # customer =
    # product = 
    
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for Delivery', 'OUT for Delivery'),
        ('Delivered', 'Delivered')
    )

    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=25, null=True, choices=STATUS)
     
    def __str__(self):
        return self.status
