from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

from academic.models import ClassRegistration
from .forms import SubjectRegistrationForm, ClassSelectMarkEntryForm, ClassSelectSubjectListForm, StudentResultForm, ResulltForm, ApprovalForm, TeacherResultsForm
from .models import SubjectRegistration, Result, StudentResult
from student.models import AcademicInfo, EnrolledStudent, currentsession
from django.forms.formsets import formset_factory
from django.contrib import messages

@login_required(login_url='login')
def add_subject(request):
    form  = SubjectRegistrationForm()
    if request.method == 'POST':
        form = SubjectRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject-list')
    context = {'form': form}
    return render(request, 'result/add-subject.html', context)

@login_required(login_url='login')
def edit_subject(request, id):
    subject = SubjectRegistration.objects.get(id=id)
    form = SubjectRegistrationForm(instance=subject)
    if request.method == 'POST':
        form = SubjectRegistrationForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subject-list')
    context = {'form': form}
    return render(request, 'result/add-subject.html', context)

@login_required(login_url='login')
def subject_list(request):
    form = ClassSelectSubjectListForm(request.GET or None)
    select_class = request.GET.get('select_class', None)
    if select_class:
        cl = ClassRegistration.objects.get(id=select_class)
        subjects = SubjectRegistration.objects.filter(select_class=cl)
        context = {'form': form, 'subjects': subjects}
        return render(request, 'result/subject-list.html', context)

    context = {'form': form}
    return render(request, 'result/subject-list.html', context)

@login_required(login_url='login')
def mark_entry(request):
    form = ClassSelectMarkEntryForm(request.GET or None)
    select_class = request.GET.get('select_class', None)
    select_subject = request.GET.get('select_class', None)
    if select_class and select_subject:
        cl = ClassRegistration.objects.get(id=select_class)
        student = EnrolledStudent.current_year.filter(class_name=cl).only('student')
        context = {'form': form, 'student': student}
        return render(request, 'result/mark-entry.html', context)
    context = {'form': form}
    return render(request, 'result/mark-entry.html', context)

@login_required(login_url='login')
def mark_table(request, subject):
    return render(request, 'result/mark-table.html')

@login_required(login_url='login')
def mark_result(request):
    form = StudentResultForm
    if request.method == 'POST':
        form = StudentResultForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'result/mark-result.html', context)    

@login_required(login_url='login')
def my_subjects(request):
    subjects = SubjectRegistration.objects.filter(teacher__login_details = request.user)
    context = {
        'subjects': subjects
    }    
    return render(request, 'result/my-subjects.html', context)

def teacher_result(request, subject_code):
    subject = SubjectRegistration.objects.get(subject_code=subject_code)
    students = EnrolledStudent.current_year.filter(class_name=subject.select_class)
    result_formset = formset_factory(ResulltForm, extra=students.count()) 
    if request.method == 'POST':
        results = result_formset(request.POST)
        if results.is_valid():
            for student, result in zip(students, results):
                result = result.save(commit=False)
                result.subject = subject
                result.student = student
                try:
                    result.save()
                    messages.info(request, 'Results have been created successfully')
                    return redirect('home')
                except IntegrityError:
                    messages.info(request, 'This result has already been created')

    list = zip(students, result_formset())
    context = {
        'list': list, 
        'subject': subject,
        'result_formset': result_formset,
    }
    return render(request, 'result/teacher-result.html', context)


@login_required(login_url='login')
def student_result(request, registration_no):
    student = EnrolledStudent.current_year.get(student__registration_no=registration_no)
    results = Result.objects.filter(student=student)
    form = TeacherResultsForm()
    if request.method == 'POST':
        form = TeacherResultsForm(request.POST)
        if form.is_valid():
            teacher_comment = form.cleaned_data['teacher_comment']
            principal_comment = form.cleaned_data['principal_comment']
            total = 0
            stu = StudentResult.objects.create(student=student, teacher_comment=teacher_comment, principal_comment=principal_comment)
            for result in results:
                stu.result.add(result)  
            stu.save()   
            messages.info(request, 'Result created successfully')    
            return redirect('home')
                                
    context = {
        'student': student,
        'results': results,
        'form': form,
    }
    return render(request, 'result/student-result-prep.html', context)

@login_required(login_url='login')
def students_list(request):
    classw = ClassRegistration.objects.get(guide_teacher__login_details = request.user)
    students = EnrolledStudent.current_year.filter(class_name=classw)
    context = {
        'class': classw,
        'students': students,
    }
    return render(request, 'result/students-list.html', context)

@login_required(login_url='login')
def student_results_list(request, registration_no):
    try:
        student = EnrolledStudent.objects.filter(student__registration_no=registration_no)
        result = StudentResult.objects.filter(student__in=student)
    except:
        messages.info(request, 'No results available')
        return redirect('home')    
    context = {
        'student': student,
        'result': result
    }
    return render(request, 'result/students-results-list.html', context)


@login_required(login_url='login')
def approve_students_result(request):
    try:
        session = currentsession.objects.get()
        results = StudentResult.objects.filter(student__session=session.current)
    except:
        messages.info(request, 'No results available')
        return redirect('home')
        results = None
        
    if request.method == 'POST':
        for result in results:
            for i,x in enumerate(sorted([result.total_points for result in results ], reverse = True)):
                if result.total_points == x:
                    result.position = i + 1
                    result.approval = True
                    result.save() 
    context = {
        'results': results,
    }
    return render(request, 'result/student-results.html', context) 

@login_required(login_url='login')
def result_view_list(request):
    try:
        result = StudentResult.objects.filter(student__student__login_details=request.user).only('student')
    except:
        messages.info(request, 'No results available')
        return redirect('home')    
    context = {
        'results': result
    }
    return render(request, 'result/result-view-list.html', context)

@login_required(login_url='login')
def student_result_view(request, id):
    try:
        result = StudentResult.objects.get(id=id)
    except:
        messages.info(request, "Couldn't find result")
        return redirect('home')    
    context = {
        'result': result
    }
    return render(request, 'result/student-view-result.html', context)

@login_required(login_url='login')
def result_render_pdf(request, id):
    path = "result/student-view-result.html"
    context = {"result" : StudentResult.objects.get(id=id)}

    html = render_to_string('result/student-view-result.html',context)
    io_bytes = BytesIO()
    
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), io_bytes)
    
    if not pdf.err:
        return HttpResponse(io_bytes.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse("Error while rendering PDF", status=400)    


@login_required(login_url='login')
def student_subject_result(request, name, registration_no):
    labels = []
    data = []
    results = Result.objects.filter(subject__subject_name=name, student__student__registration_no = registration_no)
    for r in results:
        data.append(r.total_score)
        labels.append(r.student.session.term)
    context = {
        'data': data,
        'labels': labels,
        'results': results
    }
    return render(request, 'result/student-subject-result.html', context)   





