from django.shortcuts import render, redirect

from teacher.models import ClassRegistration
from .forms import SubjectRegistrationForm, ClassSelectForm
from .models import SubjectRegistration

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
    form = ClassSelectForm(request.GET or None)
    select_class = request.GET.get('select_class', None)
    if select_class:
        cls = ClassRegistration.objects.get(id=select_class)
        subjects = SubjectRegistration.objects.filter(select_class=cls)
        context = {'form': form, 'subjects': subjects}
        return render(request, 'result/subject-list.html', context)

    context = {'form': form}
    return render(request, 'result/subject-list.html', context)

def mark_entry(request):
    form = ClassSelectForm()
    context = {'form': form}
    return render(request, 'result/mark-entry.html', context)
