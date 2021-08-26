from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    position = models.CharField(max_length=100, null=True)
    description = models.TextField()
    salary = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    experience = models.IntegerField(null=True)
    location = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class Candidate(models.Model):
    genderCategory = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )
    name = models.CharField(max_length=100, null=True)
    dateofbirth = models.DateField(max_length=100, null=True)
    gender = models.CharField(max_length=50, choices=genderCategory)
    mobile = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    resume = models.FileField(null=True)
    company = models.ManyToManyField(Company, blank=True)

    def __str__(self):
        return self.name







    
