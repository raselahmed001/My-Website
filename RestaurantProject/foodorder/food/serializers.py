from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
        #fields = ('first_name', 'middle_name', 'last_name', 'mobile_number', 'email')