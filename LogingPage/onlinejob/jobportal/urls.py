from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('login', views.logig),
    path('registration', views.register),
    path('dashboard', views.dashboard),

]
