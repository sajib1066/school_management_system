from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from academic.models import ClassRegistration
from student.models import EnrolledStudent
from teacher.models import PersonalInfo
from account.decorators import teacher_required
from student.models import AcademicInfo
from django.contrib import messages

@login_required(login_url='login')
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

@login_required(login_url='login')
def add_class(request):
    forms = ClassRegistrationForm()
    if request.method == 'POST':
        forms = ClassRegistrationForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('create-class')
    class_obj = ClassInfo.objects.all()
    context = {
        'forms': forms,
        'class_obj': class_obj
    }
    return render(request, 'academic/create-class.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def class_registration(request):
    forms = ClassRegistrationForm()
    if request.method == 'POST':
        forms = ClassRegistrationForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('class-list')
    context = {'forms': forms}
    return render(request, 'academic/class-registration.html', context)

@login_required(login_url='login')
def class_list(request):
    register_class = ClassRegistration.objects.all()
    context = {'register_class': register_class}
    return render(request, 'academic/class-list.html', context)


@login_required(login_url='login')
def view_session(request):
    forms = ChangeSessionForm()
    session = currentsession.objects.get()
    if request.method == 'POST':
        forms = ChangeSessionForm(request.POST)
        if forms.is_valid():
            instance = forms.save(commit=False)
            session.current = instance.current
            session.save()
            return redirect('view-session')
        context = {
        'session': session.current,
        'form': forms
                    }
    context = {'session': session.current,'form': forms}                   
    return render(request, 'academic/session.html', context)  

@login_required(login_url='login')
@teacher_required
def view_class(request):
    try:
        my_class = ClassRegistration.objects.get(guide_teacher__login_details=request.user)
        my_students = EnrolledStudent.current_year.filter(class_name=my_class).only('student')
    except:
        my_class = None 
        my_students = None       
    context = {
        'class': my_class,
        'students': my_students
    }
    return render(request, 'academic/view-class.html', context)
    

@login_required(login_url='login')
def PromoteStudent(request):
    form = SelectClassForm()
    class_name = request.GET.get('select_class', None)
    if request.method == 'POST':
        student_id = request.POST['id']
        student = AcademicInfo.objects.get(id=student_id)
        if student.class_name < 16:
            student.class_name += 1
            student.save()
            messages.success(request, 'Student Promoted Successfully')
            return redirect('promote-students')
        else:
            messages.error(request, 'Student is in final year')
            return redirect('promote-students')    
    if class_name:
        students = AcademicInfo.objects.filter(class_name=class_name)
    else:
        students = None
    context = {
        'students': students,
        'form': form
    }        
    return render(request, 'academic/promote-students.html', context)