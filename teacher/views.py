from django.shortcuts import render

# Create your views here.

def teacher_registration(request):
    return render(request, 'teacher/teacher-registration.html')

def teacher_list(request):
    return render(request, 'teacher/teacher-list.html')
