from django.urls import path

from . import views

urlpatterns = [
    path('users', views.users, name='Users'),
    path('add_user', views.add_user, name='Add User'),
    path('supervisiors', views.supervisiors, name='Supervisior'),
    path('view_user/<int:user_id>', views.view_user, name='View User'),
    path('view_user/update_user/<int:user_id>', views.update_user, name='Update User'),
]
