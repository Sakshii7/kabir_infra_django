from django.urls import path

from . import views

urlpatterns = [
    path('clients', views.clients, name='View Clients'),
    path('add_clients', views.add_clients, name='Add Clients'),
    path('view_clients/<int:client_id>', views.view_clients, name='View Clients'),
    path('view_clients/update_clients/<int:client_id>', views.update_clients, name='Update Clients'),
]
