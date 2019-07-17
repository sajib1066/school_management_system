from django.shortcuts import render, redirect
from teacher.models import ClassRegistration
# Create your views here.
from .forms import AcademicInfoForm
from .models import AcademicInfo

def class_wise_student_registration(request):
    register_class = ClassRegistration.objects.all()
    context = {'register_class': register_class}
    return render(request, 'student/class-wise-student-registration.html', context)

def student_registration(request, class_id):
    cr = ClassRegistration.objects.get(id=class_id)
    academic_info_form = AcademicInfoForm()
    context = {'academic_info_form': academic_info_form, 'cr': cr}
    return render(request, 'student/student-registration.html', context)

def student_list(request, class_id):
    student = AcademicInfo.objects.get(id=class_id)
    context = {'student': student}
    return render(request, 'student/student-list.html', context)
