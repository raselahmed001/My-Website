from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomerSerializer
from .models import Customer


# Create your views here.

@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        "Customer List": '/customer-list/',
        "Customer Details": '/customer-details/',
        "Customer Update": '/customer-update/',
        "Customer Create": '/customer-create/',
    }
    return Response(api_urls)
@api_view(['GET'])
def Customer_List(request):
    customer = Customer.objects.all()
    serializer = CustomerSerializer(customer, many=True)
    
    return Response(serializer.data)


@api_view(['POST'])
def Create_User(request):
    serializer = CustomerSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def customer_details(request, pk):
    customer = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(customer, many=False)
    return Response(serializer.data)