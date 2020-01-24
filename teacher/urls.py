from django.urls import path

from . import views

urlpatterns = [
    path('registration', views.teacher_registration, name='teacher-registration'),
    path('list', views.teacher_list, name='teacher-list'),
    path('profile/<teacher_id>', views.teacher_profile, name='teacher-profile'),
    path('delete/<teacher_id>', views.teacher_delete, name='teacher-delete'),
    path('edit/<teacher_id>', views.teacher_edit, name='teacher-edit'),
    path('load-upazilla', views.load_upazilla, name='load-upazilla'),
]
