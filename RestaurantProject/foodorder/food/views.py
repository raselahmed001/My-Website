"""
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status

from rest_framework import generics
from rest_framework.response import Response
from .serializers import *

from .models import *


# Create your views here.

@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        "Customer List": '/customer-list/',
        "Customer Detail": '/customer-detail/<str:pk>/',
        "Customer Update": '/customer-update/<str:pk>/',
        "Customer Create": '/customer-create/<str:pk>/',
        "Customer Delete": '/customer-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def Customer_List(request):
    customer = Customer.objects.all()
    serializer = CustomerSerializer(customer, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail (reques, pk):
    customer = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(customer, many=False)
    return Response(serializer.data)



@api_view(['POST'])
def Create_User(request):
    serializer = CustomerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def CustomerUpdate(request, pk):
    customer = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(instance=customer, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def CustomerDelete(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.delete()
    return Response("Successfully delete")

"""

''''
from rest_framework import generics
from rest_framework.response import Response

from .models import *
from .serializers import *


class SocialList(generics.ListAPIView):
    queryset = Socialmedia.objects.all()
    serializer_class = SocialSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = SocialSerializer(queryset, many=True)
        return Response(serializer.data)


class SocialLinkCreate(generics.ListCreateAPIView):
    queryset = Socialmedia.objects.all()
    serializer_class = SocialSerializer


class SocialLinkUpdate(generics.UpdateAPIView):
    queryset = Socialmedia.objects.all()
    serializer_class = SocialSerializer


class SocialLinkDeleted(generics.RetrieveDestroyAPIView):
    queryset = Socialmedia.objects.all()
    serializer_class = SocialSerializer


class SocialLinkDetails(generics.RetrieveAPIView):
    queryset = Socialmedia.objects.all()
    serializer_class = SocialSerializer
'''