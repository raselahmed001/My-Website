from django.db import models

# Create your models here.

class Chef(models.Model):
    chef_name = models.CharField(max_length=100)
    chef_id = models.IntegerField()
    salary = models.FloatField()

    def __str__(self):
        return self.chef_name

class Meal(models.Model):
    name = models.CharField(max_length=45)
    meal_id = models.CharField(max_length=15)
    price = models.DecimalField(max_digits=10, decimal_places=3, default=0.0)
    Chef_chef_id = models.ManyToOneRel(to=Chef, field_name=id, field=id)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    supplier_name = models.CharField(max_length=50)
    supplier_id = models.IntegerField()
    phone = models.CharField(max_length=15)
    Chef_chef_id = models.ManyToOneRel(to=Chef, field_name=id, field=id)
    supplier_city = models.CharField(max_length=100)

    def __str__(self):
        return self.supplier_name


class Waiter(models.Model):
    name = models.CharField(max_length=100)
    waiter_id = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    attribute = models.TextField()

    def __str__(self):
        return self.name


class Customer_Info(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_id = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    location = models.TextField()
    Waiter_waiter_id = models.ManyToOneRel(to=Waiter,field_name=id, field=id)

    def __str__(self):
        return self.customer_name



class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    ingredient_id= models.CharField(max_length=100)
    discription = models.TextField()
    Meal_meal_id = models.ManyToOneRel(to=Meal, field_name=id, field=id)

    def __str__(self):
        return self.name

class Order(models.Model):
    Customer_Info_customer_id = models.ManyToOneRel(to=Customer_Info, field_name=id, field=id)
    Meal_meal_id = models.ManyToOneRel(to=Meal, field_name=id, field=id)

    def __str__(self):
        return self.Customer_Info_customer_id

class Provides(models.Model):
    Supplier_supplier_id = models.ManyToOneRel(to=Supplier, field_name=id, field=id)
    Ingredient_ingredient_id = models.ManyToOneRel(to=Ingredient, field_name=id, field=id)

    def __str__(self):
        return self.Ingredient_ingredient_id













