
from django.urls import path
from .import views

'''
urlpatterns = [
    path("", views.apiOverView, name="api-overview"),
    path("customer-list/", views.Customer_List, name="customer-list"),
    path("customer-detail/<str:pk>/", views.detail, name="customer-detail"),
    path("customer-create/", views.Create_User, name="customer-create"),
    path("customer-update/<str:pk>/", views.CustomerUpdate, name="customer-update"),
    path("customer-delete/<str:pk>/", views.CustomerDelete, name="customer-delete"),


]
'''
''''
urlpatterns = [
    path("social-list/", views.SocialList.as_view(), name="social-list"),
    path("social-create/", views.SocialLinkCreate.as_view(), name="social-create"),
    path("social-update/", views.SocialLinkUpdate.as_view(), name="social-update"),
    path("social-delete/<str:pk>/", views.SocialLinkDeleted.as_view(), name="social-delete"),
    path("social-detail/<str:pk>/", views.SocialLinkDetails.as_view(), name="social-detail"),

]
'''