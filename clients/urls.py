from django.urls import path
from . import views

urlpatterns = [
    path('clients', views.clients, name='View Clients'),
    path('add_clients', views.add_clients, name='Add Clients'),
]