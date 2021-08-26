from django.db import models


# Create your models here.
class Socialmedia(models.Model):
    social_name = models.CharField(max_length=10, null=True, blank=True)
    facebook_link = models.CharField(max_length=200, null=True, blank=True)
    twitter_link = models.CharField(max_length=200, null=True, blank=True)
    instagram_link = models.CharField(max_length=200, null=True, blank=True)
    linkedin_link = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return "social_name"


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField()
    social = models.OneToOneField(Socialmedia, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    user_image = models.ImageField(upload_to="images/user_cus/")

    def __str__(self):
        return self.first_name



class Marchent(models.Model):
    owner_name = models.CharField(max_length=100)
    no_of_restaurant = models.IntegerField(null=True, blank=True)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=20)
    telephone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField()
    social = models.OneToOneField(Socialmedia, on_delete=models.CASCADE)
    mar_image = models.FileField(upload_to="images/mar_image/")
    nid_driving_lic_image = models.ImageField(upload_to="images/nid/")
    res_date = models.DateTimeField(auto_now_add=True)
    validation_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.owner_name


class Restaurant(models.Model):
    mar_id = models.OneToOneField(Marchent, on_delete=models.CASCADE, null=True, blank=True)
    res_name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="images/logo/")
    banner = models.ImageField(upload_to="images/banner/")
    email = models.EmailField()
    mobile_number = models.CharField(max_length=20)
    telephone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField()
    lit = models.CharField(max_length=200)
    long = models.CharField(max_length=200)
    social = models.OneToOneField(Socialmedia, on_delete=models.CASCADE)
    trade_lic_image = models.FileField(upload_to="images/trade_lic/")
    lic_validation_date = models.DateTimeField(null=True, blank=True)
    res_validation_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.res_name


