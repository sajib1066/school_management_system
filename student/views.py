from django.shortcuts import render, redirect
from academic.models import ClassRegistration
from .forms import *
from .models import *

def load_upazilla(request):
    district_id = request.GET.get('district')
    upazilla = Upazilla.objects.filter(district_id=district_id).order_by('name')

    upazilla_id = request.GET.get('upazilla')
    union = Union.objects.filter(upazilla_id=upazilla_id).order_by('name')
    context = {
        'upazilla': upazilla,
        'union': union
    }
    return render(request, 'others/upazilla_dropdown_list_options.html', context)


def class_wise_student_registration(request):
    register_class = ClassRegistration.objects.all()
    context = {'register_class': register_class}
    return render(request, 'student/class-wise-student-registration.html', context)

def student_registration(request):
    academic_info_form = AcademicInfoForm(request.POST or None)
    personal_info_form = PersonalInfoForm(request.POST or None, request.FILES or None)
    student_address_info_form = StudentAddressInfoForm(request.POST or None)
    guardian_info_form = GuardianInfoForm(request.POST or None)
    emergency_contact_details_form = EmergencyContactDetailsForm(request.POST or None)
    previous_academic_info_form = PreviousAcademicInfoForm(request.POST or None)
    previous_academic_certificate_form = PreviousAcademicCertificateForm(request.POST or None, request.FILES)

    if request.method == 'POST':
        if academic_info_form.is_valid() and personal_info_form.is_valid() and student_address_info_form.is_valid() and guardian_info_form.is_valid() and emergency_contact_details_form.is_valid() and previous_academic_info_form.is_valid() and previous_academic_certificate_form.is_valid():
            s1 = personal_info_form.save()
            s2 = student_address_info_form.save()
            s3 = guardian_info_form.save()
            s4 = emergency_contact_details_form.save()
            s5 = previous_academic_info_form.save()
            s6 = previous_academic_certificate_form.save()
            academic_info = academic_info_form.save(commit=False)
            academic_info.personal_info = s1
            academic_info.address_info = s2
            academic_info.guardian_info = s3
            academic_info.emergency_contact_info = s4
            academic_info.previous_academic_info = s5
            academic_info.previous_academic_certificate = s6
            academic_info.save()
            return redirect('student-list')

    context = {
        'academic_info_form': academic_info_form,
        'personal_info_form': personal_info_form,
        'student_address_info_form': student_address_info_form,
        'guardian_info_form': guardian_info_form,
        'emergency_contact_details_form': emergency_contact_details_form,
        'previous_academic_info_form': previous_academic_info_form,
        'previous_academic_certificate_form': previous_academic_certificate_form
    }
    return render(request, 'student/student-registration.html', context)

def student_list(request):
    student = AcademicInfo.objects.filter(is_delete=False).order_by('-id')
    context = {'student': student}
    return render(request, 'student/student-list.html', context)

def student_profile(request, student_id):
    student = AcademicInfo.objects.get(id=student_id)
    context = {
        'student': student
    }
    return render(request, 'student/student-profile.html', context)

def student_edit(request, student_id):
    student = AcademicInfo.objects.get(id=student_id)
    academic_info_form = AcademicInfoForm(instance=student)
    personal_info_form = PersonalInfoForm(instance=student.personal_info)
    student_address_info_form = StudentAddressInfoForm(instance=student.address_info)
    guardian_info_form = GuardianInfoForm(instance=student.guardian_info)
    emergency_contact_details_form = EmergencyContactDetailsForm(instance=student.emergency_contact_info)
    previous_academic_info_form = PreviousAcademicInfoForm(instance=student.previous_academic_info)
    previous_academic_certificate_form = PreviousAcademicCertificateForm(instance=student.previous_academic_certificate)

    if request.method == 'POST':
        academic_info_form = AcademicInfoForm(request.POST, instance=student)
        personal_info_form = PersonalInfoForm(request.POST, request.FILES, instance=student.personal_info)
        student_address_info_form = StudentAddressInfoForm(request.POST, instance=student.address_info)
        guardian_info_form = GuardianInfoForm(request.POST, instance=student.guardian_info)
        emergency_contact_details_form = EmergencyContactDetailsForm(request.POST, instance=student.emergency_contact_info)
        previous_academic_info_form = PreviousAcademicInfoForm(request.POST, instance=student.previous_academic_info)
        previous_academic_certificate_form = PreviousAcademicCertificateForm(request.POST, request.FILES, instance=student.previous_academic_certificate)
        if academic_info_form.is_valid() and personal_info_form.is_valid() and student_address_info_form.is_valid() and guardian_info_form.is_valid() and emergency_contact_details_form.is_valid() and previous_academic_info_form.is_valid() and previous_academic_certificate_form.is_valid():
            s1 = personal_info_form.save()
            s2 = student_address_info_form.save()
            s3 = guardian_info_form.save()
            s4 = emergency_contact_details_form.save()
            s5 = previous_academic_info_form.save()
            s6 = previous_academic_certificate_form.save()
            academic_info = academic_info_form.save(commit=False)
            academic_info.personal_info = s1
            academic_info.address_info = s2
            academic_info.guardian_info = s3
            academic_info.emergency_contact_info = s4
            academic_info.previous_academic_info = s5
            academic_info.previous_academic_certificate = s6
            academic_info.save()
            return redirect('student-list')

    context = {
        'academic_info_form': academic_info_form,
        'personal_info_form': personal_info_form,
        'student_address_info_form': student_address_info_form,
        'guardian_info_form': guardian_info_form,
        'emergency_contact_details_form': emergency_contact_details_form,
        'previous_academic_info_form': previous_academic_info_form,
        'previous_academic_certificate_form': previous_academic_certificate_form
    }
    return render(request, 'student/student-edit.html', context)

def student_delete(request, student_id):
    student = AcademicInfo.objects.get(id=student_id)
    student.is_delete = True
    student.save()
    return redirect('student-list')

def student_search(request):
    try:
        search = StudentSearchForm()
        registration = request.GET.get('registration_no' or None)
        student = AcademicInfo.objects.get(registration_no=registration)
        context = {
            'search': search,
            'student': student
        }
        return render(request, 'student/student-search.html', context)
    except Exception as e:
        print(e)
    context = {
            'search': search
        }
    return render(request, 'student/student-search.html', context)
