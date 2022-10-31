from django.urls import path

from . import views

urlpatterns = [
    path('', views.material_requisition, name='Material Requisition List'),
    path('add_material_requisition', views.add_material_requisition, name='Add Material Requisition'),
    path('view_material_req/<int:req_id>', views.view_material_req, name='View Material Requisition'),
    path('view_material_req/update_record/<int:req_id>', views.update_material_req, name='Update Material Requisition'),
    # path('pdf_view', views.pdf_view, name='Add Material Requisition'),
]
