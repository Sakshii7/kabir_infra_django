from django.urls import path

from . import views

urlpatterns = [
    path('sites', views.sites, name='Sites'),
    path('add_sites', views.add_sites, name='Add Sites'),
    path('load_states', views.load_states, name='load_states'),
    path('load_city', views.load_city, name='load_city'),
    path('view_sites/<int:site_id>', views.view_sites, name='View Sites'),
    path('view_sites/update_sites/<int:site_id>', views.update_sites, name='Update Sites'),
]
