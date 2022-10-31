from django.urls import path

from . import views

urlpatterns = [
    path('materials', views.materials, name='View Materials'),
    path('add_materials', views.add_materials, name='Add Materials'),
    path('view_materials/<int:material_id>', views.view_materials, name='View Materials'),
    path('view_materials/update_materials/<int:material_id>', views.update_materials, name='Update Materials'),
]
