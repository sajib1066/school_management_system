from django.urls import path
from .views import student_attendance, set_attendance

urlpatterns = [
    path('student/', student_attendance, name='student-attendance'),
    path('set-attendance/<std_class>/<std_roll>', set_attendance, name='set-attendance')
]