from django.urls import path
from . import views

urlpatterns = [
    path('', views.materials, name='Material Requisition List'),
    path('homepage', views.homepage, name='Homepage'),
    path('add_material_requisition', views.add_material_requisition, name='Add Material Requisition'),
]
