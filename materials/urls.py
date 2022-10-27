from django.urls import path
from . import views

urlpatterns = [
    path('materials', views.materials, name='View Materials'),
    path('add_materials', views.add_materials, name='Add Materials'),
]
