from django.urls import path
from .views import student_attendance, SetAttendance

urlpatterns = [
    path('student/', student_attendance, name='student-attendance'),
    path('set-attendance/<std_class>/<std_roll>', SetAttendance.as_view(), name='set-attendance')
]