from django.urls import path
from . import views

urlpatterns = [
    path('class-wise-student-registration', views.class_wise_student_registration, name='class-wise-student-registration'),
    path('student-registration/<class_id>', views.student_registration, name='student-registration'),
    path('student-list/<class_id>', views.student_list, name='student-list'),

]
