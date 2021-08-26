from django.db import models


# Create your models here.

class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        # return "Name :",self.first_name ,self.last_name,self.create_at
        return self.full_name


class Tag(models.Model):
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class Category(models.Model):
    name = models.CharField(max_length=500)
    #create_at = models.DateTimeField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ManyToManyField(to=Category)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    tag = models.ManyToManyField(to=Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
        ('Out of delivery', 'Out of delivery'),
    )

    customer = models.OneToOneField(to=Customer, null=True, blank=True, on_delete=models.SET_NULL)
    product = models.ManyToManyField(to=Product)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.product
