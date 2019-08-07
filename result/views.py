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
            return redirect('home')
    context = {'form': form}
    return render(request, 'result/add-subject.html', context)

def subject_list(request):
    form = ClassSelectForm()
    cls = ClassRegistration.objects.all()
    cl = request.POST.get('selectClass')

    if request.method == 'GET':
        form = ClassSelectForm()
    else:
        clsa = ClassRegistration.objects.get(cl=cl)
        sub = SubjectRegistration.objects.filter(select_class=clsa)

    context = {'form': form}
    return render(request, 'result/subject-list.html', context)
