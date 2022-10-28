from django.urls import path
from . import views

urlpatterns = [
    path('sites', views.sites, name='Sites'),
    # path('add_vendors', views.add_vendors, name='Add Vendors'),
]
