from django.urls import path

from . import views

urlpatterns = [
    path('login', views.admin_login, name='login'),
    path('logout', views.admin_logout, name='logout'),
    path('add-department', views.add_department, name='add-department'),
    path('designation', views.add_designation, name='designation'),
]
