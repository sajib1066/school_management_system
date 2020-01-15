from django.shortcuts import render, redirect

from academic.models import ClassRegistration
from .forms import SubjectRegistrationForm, ClassSelectMarkEntryForm, ClassSelectSubjectListForm
from .models import SubjectRegistration
from student.models import AcademicInfo

def add_subject(request):
    form  = SubjectRegistrationForm()
    if request.method == 'POST':
        form = SubjectRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject-list')
    context = {'form': form}
    return render(request, 'result/add-subject.html', context)

def subject_list(request):
    form = ClassSelectSubjectListForm(request.GET or None)
    select_class = request.GET.get('select_class', None)
    if select_class:
        cls = ClassRegistration.objects.get(id=select_class)
        subjects = SubjectRegistration.objects.filter(select_class=cls)
        context = {'form': form, 'subjects': subjects}
        return render(request, 'result/subject-list.html', context)

    context = {'form': form}
    return render(request, 'result/subject-list.html', context)

def mark_entry(request):
    form = ClassSelectMarkEntryForm(request.GET or None)
    select_class = request.GET.get('select_class', None)
    if select_class:
        cls = ClassRegistration.objects.get(id=select_class)
        student = AcademicInfo.objects.filter(class_info=cls)
        context = {'form': form, 'student': student}
        return render(request, 'result/mark-entry.html', context)
    context = {'form': form}
    return render(request, 'result/mark-entry.html', context)

def mark_table(request, subject):
    return render(request, 'result/mark-table.html')
