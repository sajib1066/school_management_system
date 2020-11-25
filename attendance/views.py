from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from .forms import SearchEnrolledStudentForm, AttendanceForm, DateForm
from student.models import EnrolledStudent
from academic.models import ClassRegistration
from teacher.models import PersonalInfo
from .models import StudentAttendance
from django.forms.formsets import formset_factory
from django.contrib import messages

@login_required(login_url='login')
def student_attendance(request):
    forms = SearchEnrolledStudentForm()
    class_name = request.GET.get('reg_class', None)
    if request.user.is_student:
        student = StudentAttendance.objects.filter(student__student__login_details = request.user)
        return render(request, 'attendance/my-attendance.html', {'student': student})      
    if request.method == 'POST':
        class_info = ClassRegistration.objects.get(class_name=class_name)
        student = EnrolledStudent.current_year.filter(class_name=cll)
        count = student.count()
        attendance_formset = formset_factory(AttendanceForm, extra=count)
        formset = attendance_formset(request.POST)
        dateform = DateForm(request.POST)
        if dateform.is_valid():
            date = dateform.cleaned_data['date']
        list = zip(student,formset)
        if formset.is_valid():
            for form, student in zip(formset,student):
                mark = form.cleaned_data['mark_attendance']
                try:
                    StudentAttendance.objects.create_attendance(class_info.name, student.roll, mark, date)
                except:
                    return    
            return redirect('home')
    if class_name:
        class_info = ClassRegistration.objects.get(class_name=class_name)
        student = EnrolledStudent.objects.filter(class_name=cll)
        count = student.count()
        attendance_formset = formset_factory(AttendanceForm, extra=count)
        list = zip(student, attendance_formset())
        date_form = DateForm()
        context = {
            'formset': attendance_formset,
            'forms': forms,
            'list': list,
            'class_info': class_info,
            'date_form': date_form
        }
        return render(request, 'attendance/student-attendance.html', context)
    context = {
        'forms': forms,
    }
    return render(request, 'attendance/student-attendance.html', context)

class SetAttendance(APIView):
    def get(self, request, std_class, std_roll, std_id):
        try:
            std_id = int(std_id)
            StudentAttendance.objects.create_attendance(std_class, std_roll, std_id)
            return Response({'status': 'Success'}, status=status.HTTP_200_OK)
        except:
            return Response({'status': 'Failed'}, status=status.HTTP_400_BAD_REQUEST)

@login_required(login_url='login')
def GetAttendance(request, std_class):
    forms = DateForm()
    date = request.GET.get('date', None)
    if date:
        try:
            attendance = StudentAttendance.objects.class_attendance(std_class, date)
        except:
            attendance = None
        return render(request, 'attendance/class-attendance.html', {'forms': forms, 'attendance': attendance, 'date': date, 'class': std_class})    
    return render(request, 'attendance/class-attendance.html', {'forms': forms, 'class': std_class})    

@login_required(login_url='login')
def ViewAttendance(request):
    try:
        classes = ClassRegistration.objects.all()
    except:
        classes = None    
    return render(request, 'attendance/view-attendance.html', {'classes': classes})

@login_required(login_url='login')
def TeacherAttendance(request):
    cll = ClassRegistration.objects.get(guide_teacher__login_details = request.user)
    class_name = cll.class_name 
    student = EnrolledStudent.objects.filter(class_name=cll)
    count = student.count()
    date_form = DateForm()
    if request.method == 'POST':
        attendance_formset = formset_factory(AttendanceForm, extra=count)
        formset = attendance_formset(request.POST)
        dateform = DateForm(request.POST)
        if dateform.is_valid():
            date = dateform.cleaned_data['date']
        list = zip(student,formset)
        if formset.is_valid():
            for form, studen in zip(formset,student):
                try:
                    mark = form.cleaned_data['mark_attendance']
                    StudentAttendance.objects.create_attendance(cll.name, studen.roll, mark, date)
                    messages.info('Attendance for {} marked'.format(studen.student.personal_info.name))
                except:
                    messages.info(request, 'Could not mark {} Attendance'.format(studen.student.personal_info.name))
                    return redirect('home')    
            return redirect('home')
    attendance_formset = formset_factory(AttendanceForm, extra=count)
    list = zip(student, attendance_formset())        
    context = {
        'formset': attendance_formset,
        'list': list,
        'class_info': cll,
        'date_form': date_form
        }
    return render(request, 'attendance/student-attendance.html', context)       
    
    
      

