from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import student
import teacher
import employee
import academic

@login_required(login_url='login')
def home_page(request):
    total_student = student.models.AcademicInfo.objects.count()
    total_teacher = teacher.models.PersonalInfo.objects.count()
    total_employee = employee.models.PersonalInfo.objects.count()
    total_class = academic.models.ClassRegistration.objects.count()
    context = {
        'student': total_student,
        'teacher': total_teacher,
        'employee': total_employee,
        'total_class': total_class,
    }
    return render(request, 'home.html', context)
