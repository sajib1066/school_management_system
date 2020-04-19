from django.contrib import admin
from .models import StudentAttendance

class StudentAttendanceAdmin(admin.ModelAdmin):
    list_display = ['class_name', 'student', 'date']

admin.site.register(StudentAttendance, StudentAttendanceAdmin)
