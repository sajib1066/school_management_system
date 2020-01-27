from django.urls import path
from .views import student_attendance

urlpatterns = [
    path('student/', student_attendance, name='student-attendance')
]