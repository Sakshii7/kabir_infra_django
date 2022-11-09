from django.urls import path

from . import views

urlpatterns = [
    path('country', views.country, name='Country List'),
    path('add_country', views.add_country, name='Add Country'),
    path('view_country/<int:country_id>', views.view_country, name='View Country'),
    path('view_country/update_country/<int:country_id>', views.update_country, name='Update Country'),
    path('states', views.states, name='State List'),
    path('add_state', views.add_state, name='Add State'),
    path('view_state/<int:state_id>', views.view_state, name='View State'),
    path('view_state/update_state/<int:state_id>', views.update_state, name='Update State'),
    path('city', views.city, name='City List'),
    path('add_city', views.add_city, name='add_city'),
    path('load_states', views.load_states, name='load_states'),
    path('view_city/<int:city_id>', views.view_city, name='View City'),
    path('view_city/update_city/<int:city_id>', views.update_city, name='Update City'),
]
