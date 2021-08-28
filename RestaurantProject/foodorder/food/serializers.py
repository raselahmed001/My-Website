"""
from rest_framework import serializers
from .models import *


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
        # fields = ('first_name', 'middle_name', 'last_name', 'mobile_number', 'email')


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socialmedia
        fields = "__all__"


"""