from django.urls import path

from . import views

urlpatterns = [
    path('companies', views.companies, name='Companies'),
    path('add_company', views.add_company, name='Add Company'),
    path('load_states', views.load_states, name='load_states'),
    path('load_city', views.load_city, name='load_city'),
]
