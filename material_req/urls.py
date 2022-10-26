from django.urls import path
from . import views

urlpatterns = [
    path('', views.materials, name='Material Requisition List'),
    path('add_material_requisition', views.add_material_requisition, name='Add Material Requisition'),
    # path('pdf_view', views.pdf_view, name='Add Material Requisition'),
]
