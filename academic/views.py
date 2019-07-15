from django.shortcuts import render, redirect

from .forms import *
from .models import *
# Create your views here.
def add_department(request):
    forms = DepartmentForm()
    if request.method == 'POST':
        forms = DepartmentForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('add-department')
    department = Department.objects.all()
    context = {'forms': forms, 'department': department}
    return render(request, 'academic/add-department.html', context)

def add_class(request):
    forms = ClassForm()
    if request.method == 'POST':
        forms = ClassForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('create-class')
    class_obj = ClassInfo.objects.all()
    context = {
        'forms': forms,
        'class_obj': class_obj
    }
    return render(request, 'academic/create-class.html', context)

def create_section(request):
    forms = SectionForm()
    if request.method == 'POST':
        forms = SectionForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('create-section')
    section = Section.objects.all()
    context = {
        'forms': forms,
        'section': section
    }
    return render(request, 'academic/create-section.html', context)

def create_session(request):
    forms = SessionForm()
    if request.method == 'POST':
        forms = SessionForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('create-session')
    session = Session.objects.all()
    context = {
        'forms': forms,
        'session': session
    }
    return render(request, 'academic/create-session.html', context)

def create_shift(request):
    forms = ShiftForm()
    if request.method == 'POST':
        forms = ShiftForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('create-shift')
    shift = Shift.objects.all()
    context = {
        'forms': forms,
        'shift': shift
    }
    return render(request, 'academic/create-shift.html', context)
