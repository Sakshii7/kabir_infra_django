from django.urls import path
from . import views

urlpatterns = [
    path('vendors', views.vendors, name='Vendors'),
    path('add_vendors', views.add_vendors, name='Add Vendors'),
]
