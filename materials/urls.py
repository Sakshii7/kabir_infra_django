from django.urls import path
from . import views

urlpatterns = [
    path('view_materials', views.view_materials, name='View Materials'),
    path('add_materials', views.add_materials, name='Add Materials'),
]
