from django.urls import path
from .views import student_attendance, SetAttendance, TeacherAttendance
from . import views

urlpatterns = [
    path('student/', student_attendance, name='student-attendance'),
    path('set-attendance/<std_class>/<std_roll>/<std_id>', SetAttendance.as_view(), name='set-attendance'),
    path('attendance/<std_class>', views.GetAttendance, name='get_attendance'),
    path('view/', views.ViewAttendance, name='view_attendance'),
    path('teacher-mark', views.TeacherAttendance, name='teacher-mark-attendance')
]