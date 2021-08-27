from django.urls import path
from . import views

urlpatterns = [
    path("", views.apiOverView),
    path("customer-list/", views.customer_list)

]