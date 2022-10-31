from django.urls import path
from . import views

urlpatterns = [
    path('sites', views.sites, name='Sites'),
    path('add_sites', views.add_sites, name='Add Sites'),
]
