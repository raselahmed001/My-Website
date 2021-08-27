from django.urls import path
from . import views

urlpatterns = [
    path("", views.apiOverView),
    path("customer-list/", views.Customer_List),
    path("customer-create/", views.Create_User),
    path("customer-details/", views.customer_details),

]