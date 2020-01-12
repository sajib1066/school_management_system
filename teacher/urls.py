from django.urls import path

from . import views

urlpatterns = [
    path('registration', views.teacher_registration, name='teacher-registration'),
    path('list', views.teacher_list, name='teacher-list'),
    path('delete/<teacher_id>', views.teacher_delete, name='teacher-delete'),
    path('load-upazilla', views.load_upazilla, name='load-upazilla'),
]
