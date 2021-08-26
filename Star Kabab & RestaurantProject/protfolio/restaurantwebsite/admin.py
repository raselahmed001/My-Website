from django.contrib import admin
from .models import *

# Register your models here.
class ChefAdmin(admin.ModelAdmin):
    list_display = ['chef_name', 'chef_id']
    search_fields = ['chef_name', 'chef_id']

class Customer_InfoAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'customer_id', 'phone_number', 'location']
    list_filter = ['customer_id']
    search_fields = ['customer_name', 'customer_id']


class WaiterAdmin(admin.ModelAdmin):
    list_display = ['name', 'waiter_id', 'phone']
    list_filter = ['waiter_id']
    search_fields = ['name', 'waiter_id']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['Customer_Info_customer_id', 'Meal_meal_id']
    search_fields = ['Customer_Info_customer_id']


class MealAdmin(admin.ModelAdmin):
    list_display = ['name', 'meal_id', 'price', 'Chef_chef_id']
    search_fields = ['name', 'meal_id']

class SupplierAdmin(admin.ModelAdmin):
    search_fields = ['supplier_id', 'Chef_chef_id']


class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'discription']
    list_filter = ['Meal_meal_id']
    search_fields = ['name']


class ProvidesAdmin(admin.ModelAdmin):
    list_display = ['Supplier_supplier_id', 'Ingredient_ingredient_id']
    search_fields = ['Supplier_supplier_id', 'Ingredient_ingredient_id']


admin.site.register(Chef, ChefAdmin)
admin.site.register(Customer_Info)
admin.site.register(Waiter, WaiterAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Meal, MealAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Ingredient)
admin.site.register(Provides, ProvidesAdmin)