from django.contrib import admin

from .models import *


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']
    #filter_horizontal = ['name']



class CustomerAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'email', 'create_at']
    list_filter = ['create_at']
    search_fields = ['full_name', 'phone', 'email', 'create_at']
    filter_horizontal = ['full_name', 'phone', 'email']


class ProductAdmin(admin.ModelAdmin):
    #list_display = ['name', 'price', 'category']
    list_filter = ['price', 'category', 'tag']
    search_fields = ['name', 'category', 'price', 'tag']
    filter_horizontal = ['tag']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_date']
    list_filter = ['order_date', 'status']
    search_fields = ['customer', 'product']
    filter_horizontal = ['product']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tag)
admin.site.register(Order, OrderAdmin)
