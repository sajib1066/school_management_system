from django.shortcuts import render, redirect

from . import forms
from .models import *


# Create your views here.



def teacher_registration(request):
    form = forms.PersonalInfoForm()
    education_form = forms.EducationInfoForm()
    training_form = forms.TrainingInfoForm()
    job_form = forms.JobInfoForm()
    experience_form = forms.ExperienceInfoForm()
    if request.method == 'POST':
        form = forms.PersonalInfoForm(request.POST, request.FILES)
        education_form = forms.EducationInfoForm(request.POST)
        training_form = forms.TrainingInfoForm(request.POST)
        job_form = forms.JobInfoForm(request.POST)
        experience_form = forms.ExperienceInfoForm(request.POST)
        if form.is_valid() and education_form.is_valid() and training_form.is_valid() and job_form.is_valid() and experience_form.is_valid():
            personal_info = form.save()
            education_info = education_form.save(commit=False)
            education_info.education = personal_info
            education_info.save()
            training_info = training_form.save(commit=False)
            training_info.training = personal_info
            training_info.save()
            job_info = job_form.save(commit=False)
            job_info.job = personal_info
            job_info.save()
            experience_info = experience_form.save(commit=False)
            experience_info.experience = personal_info
            experience_info.save()
            return redirect('employee-list')

    context = {
        'form': form,
        'education_form': education_form,
        'training_form': training_form,
        'job_form': job_form,
        'experience_form': experience_form
    }
    return render(request, 'employee/employee-registration.html', context)


def teacher_list(request):
    teacher = PersonalInfo.objects.all()
    context = {'teacher': teacher}
    return render(request, 'employee/employee-list.html', context)
