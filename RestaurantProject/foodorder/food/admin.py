from django.contrib import admin
from .models import*

@admin.register(Socialmedia)

class SocialmediaAdmin(admin.ModelAdmin):
    list_display = ['social_name', 'facebook_link', 'twitter_link', 'instagram_link', 'linkedin_link']
    search_fields = ['social_name', 'facebook_link', 'twitter_link', 'instagram_link', 'linkedin_link']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'middle_name', 'last_name', 'mobile_number']
    search_fields = ['first_name', 'last_name']

@admin.register(Marchent)
class MarchentAdmin(admin.ModelAdmin):
    list_display = ['owner_name', 'no_of_restaurant', 'mobile_number', 'email', 'validation_date']
    search_fields = ['owner_name', 'email', 'mobile_number']
    list_filter = ['res_date', 'validation_date']

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['res_name', 'mar_id', 'mobile_number', 'email', 'lic_validation_date', 'res_validation_date']
    search_fields = ['res_name', 'email', 'mobile_number']
    list_filter = ['lic_validation_date', 'res_validation_date']


#admin.site.register(Socialmedia, SocialmediaAdmin)
#admin.site.register(Customer, CustomerAdmin)
#admin.site.register(Marchent, MarchentAdmin)
#admin.site.register(Restaurant, RestaurantAdmin)
