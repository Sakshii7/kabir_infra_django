from django.urls import path

from . import views

urlpatterns = [
    path('vendors', views.vendors, name='Vendors'),
    path('add_vendors', views.add_vendors, name='Add Vendors'),
    path('load_states', views.load_states, name='load_states'),
    path('load_city', views.load_city, name='load_city'),
    path('view_vendor/<int:vendor_id>', views.view_vendor, name='View Vendor'),
    path('view_vendor/update_vendor/<int:vendor_id>', views.update_vendor, name='Update Vendor'),
]
