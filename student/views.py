from django.shortcuts import render, redirect
from teacher.models import ClassRegistration
# Create your views here.
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

def student_registration(request, class_id):
    cr = ClassRegistration.objects.get(id=class_id)
    academic_info_form = AcademicInfoForm(request.POST or None)
    personal_info_form = PersonalInfoForm(request.POST or None, request.FILES)
    student_address_info_form = StudentAddressInfoForm(request.POST or None)
    guardian_info_form = GuardianInfoForm(request.POST or None)
    emergency_contact_details_form = EmergencyContactDetailsForm(request.POST or None)
    previous_academic_info_form = PreviousAcademicInfoForm(request.POST or None)
    previoud_academic_certificate_form = PreviousAcademicCertificateForm(request.POST or None)

    if request.method == 'POST':
        academic_info_form = AcademicInfoForm(request.POST)
        personal_info_form = PersonalInfoForm(request.POST, request.FILES)
        student_address_info_form = StudentAddressInfoForm(request.POST)
        guardian_info_form = GuardianInfoForm(request.POST)
        emergency_contact_details_form = EmergencyContactDetailsForm(request.POST)
        previous_academic_info_form = PreviousAcademicInfoForm(request.POST)
        previous_academic_certificate_form = PreviousAcademicCertificateForm(request.POST, request.FILES)

        if academic_info_form.is_valid() and personal_info_form.is_valid() and student_address_info_form.is_valid() and guardian_info_form.is_valid() and emergency_contact_details_form.is_valid() and previous_academic_info_form.is_valid() and previoud_academic_certificate_form.is_valid():
            academic_info = academic_info_form.save()
            personal_info = personal_info_form.save(commit=False)
            personal_info.personal_info = academic_info
            personal_info.save()
            student_address_info = student_address_info_form.save(commit=False)
            student_address_info.address_info = academic_info
            student_address_info.save()
            guardian_info = guardian_info_form.save(commit=False)
            guardian_info.guardian_info = academic_info
            guardian_info.save()
            emergency_contact_details = emergency_contact_details_form.save(commit=False)
            emergency_contact_details.emergency_contact_info = academic_info
            emergency_contact_details.save()
            previous_academic_info = previous_academic_info_form.save(commit=False)
            previous_academic_info.previous_academic_info = academic_info
            previous_academic_info.save()
            previous_academic_certificate_info = previous_academic_certificate_form.save(commit=False)
            previous_academic_certificate_info.previous_academic_certificate = academic_info
            previous_academic_certificate_info.save()
            return redirect('student-list', class_id=class_id)

    context = {
        'academic_info_form': academic_info_form,
        'personal_info_form': personal_info_form,
        'student_address_info_form': student_address_info_form,
        'guardian_info_form': guardian_info_form,
        'emergency_contact_details_form': emergency_contact_details_form,
        'previous_academic_info_form': previous_academic_info_form,
        'previoud_academic_certificate_form': previoud_academic_certificate_form,
        'cr': cr
    }
    return render(request, 'student/student-registration.html', context)

def student_list(request, class_id):
    student = AcademicInfo.objects.get(id=class_id)
    context = {'student': student}
    return render(request, 'student/student-list.html', context)
