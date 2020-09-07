from django.urls import path
from .views import student_attendance, SetAttendance, GetAttendance

urlpatterns = [
    path('student/', student_attendance, name='student-attendance'),
    path('set-attendance/<std_class>/<std_roll>/<std_id>', SetAttendance.as_view(), name='set-attendance'),
    path('attendance/<std_class>', GetAttendance.as_view(), name='get_attendance')
]