from django.shortcuts import render
from .models import *



# Create your views here.
def Index(request):
   return render(request,'index.html')

def getCategories(request):
       Categories = Category.objects.all


