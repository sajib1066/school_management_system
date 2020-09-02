from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import student
import teacher
import employee
import academic

@login_required(login_url='login')
def home_page(request):
    if request.user.is_teacher:
        teacher_personal_info = teacher.models.PersonalInfo.objects.get(login_details=request.user)
        try: 
            clas = academic.models.ClassRegistration.objects.get(guide_teacher__name =teacher_personal_info)
        except:
            clas = None
        context = {
            'teacher_personal_info': teacher_personal_info,
            'class': clas
        }
        return render(request, 'teacherhome.html', context)
    if request.user.is_student:
        student_academic_info = student.models.AcademicInfo.objects.get(login_details=request.user)
        context = {
            'academic_info': student_academic_info
        }
        return render(request, 'studenthome.html', context)

    total_student = student.models.AcademicInfo.objects.count()
    total_teacher= teacher.models.PersonalInfo.objects.count()
    total_employee = employee.models.PersonalInfo.objects.count()
    total_class = academic.models.ClassRegistration.objects.count()
    context = {
        'student': total_student,
        'teacher': total_teacher,
        'employee': total_employee,
        'total_class': total_class,
    }
    return render(request, 'home.html', context)
