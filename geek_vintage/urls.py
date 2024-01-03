from django.urls import path

#from same directory call views.py
from . import views

urlpatterns = [
    path("", views.index),
    path("lasagna.html", views.lasagna),
]