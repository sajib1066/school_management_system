from django.shortcuts import render

from teacher.models import ClassRegistration
from .forms import SubjectRegistrationForm

# Create your views here.

def class_list(request):
    register_class = ClassRegistration.objects.all()
    context = {'register_class': register_class}
    return render(request, 'result/class-list.html', context)

def add_subject(request, class_id):
    cls = ClassRegistration.objects.get(id=class_id)
    form  = SubjectRegistrationForm()
    context = {'form': form, 'cls': cls}
    return render(request, 'result/add-subject.html', context)
