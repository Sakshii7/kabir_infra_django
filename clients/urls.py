from django.urls import path
from . import views

urlpatterns = [
    path('view_clients', views.view_clients, name='View Clients'),
    path('add_clients', views.add_clients, name='Add Clients'),
]