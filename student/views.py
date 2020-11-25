from django.shortcuts import render, redirect
from academic.models import ClassRegistration
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def class_wise_student_registration(request):
    register_class = ClassRegistration.objects.all()
    context = {'register_class': register_class}
    return render(request, 'student/class-wise-student-registration.html', context)

@login_required(login_url='login')
def student_registration(request):
    academic_info_form = AcademicInfoForm(request.POST or None)
    login_creation_form = LoginCreationForm(request.POST or None)
    personal_info_form = PersonalInfoForm(request.POST or None, request.FILES or None)
    guardian_info_form = GuardianInfoForm(request.POST or None)
    emergency_contact_details_form = EmergencyContactDetailsForm(request.POST or None)
    previous_academic_info_form = PreviousAcademicInfoForm(request.POST or None)
    previous_academic_certificate_form = PreviousAcademicCertificateForm(request.POST or None, request.FILES)

    if request.method == 'POST':
        if academic_info_form.is_valid() and personal_info_form.is_valid() and guardian_info_form.is_valid() and emergency_contact_details_form.is_valid() and previous_academic_info_form.is_valid() and previous_academic_certificate_form.is_valid() and login_creation_form.is_valid():
            s1 = personal_info_form.save()
            s3 = guardian_info_form.save()
            s4 = emergency_contact_details_form.save()
            s5 = previous_academic_info_form.save()
            s6 = previous_academic_certificate_form.save()
            login_creation_form.is_student = True
            s7 = login_creation_form.save()
            academic_info = academic_info_form.save(commit=False)
            academic_info.personal_info = s1
            academic_info.guardian_info = s3
            academic_info.emergency_contact_info = s4
            academic_info.previous_academic_info = s5
            academic_info.previous_academic_certificate = s6
            academic_info.login_details = s7
            academic_info.save()
            return redirect('student-list')

    context = {
        'academic_info_form': academic_info_form,
        'personal_info_form': personal_info_form,
        'guardian_info_form': guardian_info_form,
        'emergency_contact_details_form': emergency_contact_details_form,
        'previous_academic_info_form': previous_academic_info_form,
        'previous_academic_certificate_form': previous_academic_certificate_form,
        'login_creation_form': login_creation_form
    }
    return render(request, 'student/student-registration.html', context)

@login_required(login_url='login')
def student_list(request):
    student = AcademicInfo.objects.filter(is_delete=False).order_by('-id')
    context = {'student': student}
    return render(request, 'student/student-list.html', context)

@login_required(login_url='login')
def student_profile(request, reg_no):
    student = AcademicInfo.objects.get(registration_no=reg_no)
    context = {
        'student': student
    }
    return render(request, 'student/student-profile.html', context)

@login_required(login_url='login')
def student_edit(request, reg_no):
    student = AcademicInfo.objects.get(registration_no=reg_no)
    academic_info_form = AcademicInfoForm(instance=student)
    personal_info_form = PersonalInfoForm(instance=student.personal_info)
    guardian_info_form = GuardianInfoForm(instance=student.guardian_info)
    emergency_contact_details_form = EmergencyContactDetailsForm(instance=student.emergency_contact_info)
    previous_academic_info_form = PreviousAcademicInfoForm(instance=student.previous_academic_info)
    previous_academic_certificate_form = PreviousAcademicCertificateForm(instance=student.previous_academic_certificate)

    if request.method == 'POST':
        academic_info_form = AcademicInfoForm(request.POST, instance=student)
        personal_info_form = PersonalInfoForm(request.POST, request.FILES, instance=student.personal_info)
        guardian_info_form = GuardianInfoForm(request.POST, instance=student.guardian_info)
        emergency_contact_details_form = EmergencyContactDetailsForm(request.POST, instance=student.emergency_contact_info)
        previous_academic_info_form = PreviousAcademicInfoForm(request.POST, instance=student.previous_academic_info)
        previous_academic_certificate_form = PreviousAcademicCertificateForm(request.POST, request.FILES, instance=student.previous_academic_certificate)
        if academic_info_form.is_valid() and personal_info_form.is_valid() and student_address_info_form.is_valid() and guardian_info_form.is_valid() and emergency_contact_details_form.is_valid() and previous_academic_info_form.is_valid() and previous_academic_certificate_form.is_valid():
            s1 = personal_info_form.save()
            s3 = guardian_info_form.save()
            s4 = emergency_contact_details_form.save()
            s5 = previous_academic_info_form.save()
            s6 = previous_academic_certificate_form.save()
            academic_info = academic_info_form.save(commit=False)
            academic_info.personal_info = s1
            academic_info.guardian_info = s3
            academic_info.emergency_contact_info = s4
            academic_info.previous_academic_info = s5
            academic_info.previous_academic_certificate = s6
            academic_info.save()
            return redirect('student-list')

    context = {
        'academic_info_form': academic_info_form,
        'personal_info_form': personal_info_form,
        'guardian_info_form': guardian_info_form,
        'emergency_contact_details_form': emergency_contact_details_form,
        'previous_academic_info_form': previous_academic_info_form,
        'previous_academic_certificate_form': previous_academic_certificate_form
    }
    return render(request, 'student/student-edit.html', context)

@login_required(login_url='login')
def student_delete(request, reg_no):
    student = AcademicInfo.objects.get(registration_no=reg_no)
    student.is_delete = True
    student.save()
    return redirect('student-list')

@login_required(login_url='login')
def student_search(request):
    forms = StudentSearchForm()
    cls_name = request.GET.get('class_name', None)
    reg_no = request.GET.get('registration_no', None)
    if cls_name:
        student = AcademicInfo.objects.filter(class_name=cls_name)
        if reg_no:
            student = student.filter(registration_no=reg_no)
        context = {
            'forms': forms,
            'student': student
        }
        return render(request, 'student/student-search.html', context)
    else:
        student = AcademicInfo.objects.filter(registration_no=reg_no)
        context = {
            'forms': forms,
            'student': student
        }
        return render(request, 'student/student-search.html', context)
    context = {
            'forms': forms,
            'student': student
        }
    return render(request, 'student/student-search.html', context)


@login_required(login_url='login')
def enrolled_student(request):
    forms = EnrolledStudentForm()
    cls = request.GET.get('class_name', None)
    student = AcademicInfo.objects.filter(class_name=cls, status='not enroll')
    context = {
        'forms': forms,
        'student': student
    }
    return render(request, 'student/enrolled.html', context)

@login_required(login_url='login')
def student_enrolled(request, reg):
    student = AcademicInfo.objects.get(registration_no=reg)
    forms = StudentEnrollForm()
    if request.method == 'POST':
        forms = StudentEnrollForm(request.POST)
        if forms.is_valid():
            roll = forms.cleaned_data['roll_no']
            class_name = forms.cleaned_data['class_name']
            session = currentsession.objects.get()
            session = session.current
            EnrolledStudent.objects.create(class_name=class_name, student=student, roll=roll, session=session)
            student.status = 'enrolled'
            student.save()
            return redirect('enrolled-student-list')
    context = {
        'student': student,
        'forms': forms
    }
    return render(request, 'student/student-enrolled.html', context)

@login_required(login_url='login')
def enrolled_student_list(request):
    student = EnrolledStudent.current_year.all()
    forms = SearchEnrolledStudentForm()
    class_name = request.GET.get('reg_class', None)
    roll = request.GET.get('roll_no', None)
    if class_name:
        student = EnrolledStudent.current_year.filter(class_name=class_name)
    context = {
        'forms': forms,
        'student': student
    }
    return render(request, 'student/enrolled-student-list.html', context)
