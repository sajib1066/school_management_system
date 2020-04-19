from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import SearchEnrolledStudentForm
from student.models import EnrolledStudent
from academic.models import ClassRegistration
from .models import StudentAttendance

def student_attendance(request):
    forms = SearchEnrolledStudentForm()
    class_name = request.GET.get('reg_class', None)
    if class_name:
        class_info = ClassRegistration.objects.get(id=class_name)
        student = EnrolledStudent.objects.filter(class_name=class_name)
        context = {
            'forms': forms,
            'student': student,
            'class_info': class_info
        }
        return render(request, 'attendance/student-attendance.html', context)
    context = {
        'forms': forms,
    }
    return render(request, 'attendance/student-attendance.html', context)

@api_view()
def set_attendance(request, std_class, std_roll):
    try:
        StudentAttendance.objects.create_attendance(std_class, std_roll)
        return Response({'status': 'Success'})
    except Exception as e:
        return Response({'status': 'Failed'})

