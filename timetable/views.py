from django.shortcuts import render, redirect
from academic.models import ClassRegistration
from result.models import SubjectRegistration
from .models import *
from . import forms
from django.contrib import messages
import random
from datetime import datetime, date, timedelta
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def AddPeriod(request):
    try:
        time = Period.objects.all().order_by('section')
    except:
        time = None 
    breakform = forms.BreakForm()           
    form = forms.PeriodForm()
    if request.method == 'POST':
        form1 = forms.PeriodForm(request.POST)
        if form1.is_valid():
            form = form1.save(commit=False)
            form.start_time = (datetime.combine(date.today(),form.start_time) + timedelta(seconds=1)).time() 
            form.save()
            messages.info(request, 'Form saved successfully')
            return redirect('add-period')
        else: 
            messages.error(request, "Couldn't save form")    
    context = {
        'form': form,
        'periods': time,
        'breakform': breakform,
    }
    return render(request, 'timetable/add-period.html', context)

@login_required(login_url='login')
def AddBreak(request):
    if request.method == 'POST':
        form = forms.BreakForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Break added successfully')
            return redirect('add-period')

@login_required(login_url='login')
def DeletePeriod(request):
    if request.method == 'POST':
        id = request.POST['id']
        Period.objects.get(id=id).delete()
        messages.success(request, 'Period deleted successfully')
        return redirect('home')

@login_required(login_url='login')
def DeleteTimetableTeacher(request):
    if request.method == 'POST':
        id = request.POST['id']
        Teacher.objects.get(id=id).delete()
        messages.success(request, 'Teacher deleted successfully')
        return redirect('add-timetable-teacher')        

@login_required(login_url='login')
def GenerateTimetable(request):
    if request.method == 'POST':
        idf = request.POST["timetable_class_id"]
        classes = ClassRegistration.objects.get(id=idf)
        classs = Class_Subjects.objects.get(class_name=classes.class_name)
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        class_periods = list(Period.objects.filter(section=classs.section).order_by('start_time'))
        break_time = Breaks.objects.get(section=classs.section, break_type='Short Break')
        before_break = Period.objects.filter(section=classs.section, start_time__lte=break_time.start_time).count()
        if Timetable.objects.filter(school_class__id=idf).count() != 0:
            Timetable.objects.filter(school_class__id=idf).delete()
        for subject in classs.subjects.all():
            DupNum = 0
            y = 0
            m = 0
            j = 0
            d = 0
            good_day = True
            if DupNum > len(class_periods):
                messages.info(request, "Couldn't create Timetable")
                redirect('home')
            while y < subject.no_of_times_a_week:
                if DupNum > len(class_periods) * 6:
                    messages.info(request, "Could not get a Timetable slot for {}, {} time".format(subject.subject.subject_name, y+1))
                    break
                else:
                    if DupNum < 3:
                        if subject.is_before_short_break and m < 3:
                            i = random.randint(0, before_break-1)                   
                        else:
                            i = random.randint(0, len(class_periods)-1)
                        d = random.randint(0, len(days)-1)    
                    else:
                        if DupNum == 3:
                            d = -1
                        if j <= len(class_periods):
                            if j == len(class_periods) and d < (len(days) - 1):
                                d += 1
                                j = 0
                            elif j < len(class_periods):
                                i = j
                                j += 1
                start_conflict = Timetable.objects.filter(school_class=classes, day=days[d],
                    period__start_time__range=(class_periods[i].start_time,
                                    class_periods[i].end_time))
                end_conflict = Timetable.objects.filter(school_class=classes, day=days[d],
                period__end_time__range=(class_periods[i].start_time,
                                class_periods[i].end_time))

                during_conflict = Timetable.objects.filter(school_class=classes,day=days[d],
                    period__start_time__gte=class_periods[i].start_time, 
                    period__end_time__lte=class_periods[i].end_time)

                teacher_start_conflict = Timetable.objects.filter(day=days[d], subject__teacher=subject.teacher,
                       period__start_time__range=(class_periods[i].start_time,
                                    class_periods[i].end_time))

                teacher_end_conflict = Timetable.objects.filter(day=days[d], subject__teacher=subject.teacher,
                       period__end_time__range=(class_periods[i].start_time,
                                    class_periods[i].end_time))                                    

                subject_conflict = Timetable.objects.filter(school_class=classes,day=days[d], subject__name=subject.name)

                for day in subject.teacher.unavailable_days.all():
                    if day.day == days[d]:
                        good_day = False  

                if subject.additional_teacher:
                    for s in subject.additional_teacher.all():
                        s_start_conflict = Timetable.objects.filter(day=days[d], subject__teacher=s,
                       period__start_time__range=(class_periods[i].start_time,
                                    class_periods[i].end_time))

                        s_end_conflict = Timetable.objects.filter(day=days[d], subject__teacher=s,
                       period__end_time__range=(class_periods[i].start_time,
                                    class_periods[i].end_time)) 

                        if s_end_conflict.count() != 0 or s_start_conflict.count() != 0:
                            good_day = False             


                if start_conflict.count() == 0 and end_conflict.count() == 0 and during_conflict.count() == 0 and teacher_start_conflict.count() == 0 and teacher_end_conflict.count() == 0 and subject_conflict.count() == 0 and good_day:
                    Timetable.objects.create(school_class=classes, subject=subject, period=class_periods[i], day=days[d], teacher=subject.teacher)
                    DupNum = 0
                    y+=1
                    m=0
                    j=0
                else:
                    DupNum += 1 
                    m += 1       

    sections = ClassRegistration.objects.all()
    context = {'register_class': sections}
    return render(request, 'timetable/time_class-list.html', context)    


@login_required(login_url='login')
def timetable_class_list(request):
    try:
        register_class = ClassRegistration.objects.all()
    except:
        messages.info(request, 'No current classes')
        redirect('home')    
    context = {'register_class': register_class}
    return render(request, 'timetable/time_class-list.html', context)


@login_required(login_url='login')
def ViewTimetable(request, id):
    classs = ClassRegistration.objects.get(id=id)
    timetable = Timetable.objects.filter(school_class__id=id)
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    periods = Period.objects.filter(section=classs.section)
    context = {
        'class': classs,
        'timetable': timetable,
        'days': days,
        'periods': periods,
    }
    return render(request, 'timetable/timetable.html', context)

@login_required(login_url='login')
def Edit_Timetable(request, id):
    if request.method == 'POST':
        form = forms.TimetableForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            day = form.cleaned_data['day']
            period = form.cleaned_data['period']
            start_confilct = Timetable.objects.filter(subject__teacher=subject.teacher, day=day, period__start_time__range=(period.start_time, period.end_time))
            end_confilct = Timetable.objects.filter(subject__teacher=subject.teacher, day=day, period__end_time__range=(period.start_time, period.end_time))
            if start_confilct.count != 0 or end_confilct.count != 0:
                messages.info(request, 'A subject exists at this time')
                return
            form.save()    
    timetable =  Timetable.objects.get(id=id)
    form = forms.TimetableForm(instance=timetable)
    context = {
        'form': form
    }
    return render(request, 'timetable/edit-timetable.html', context)

@login_required(login_url='login')
def AddSectionSubject(request):
    form = forms.SectionSubjectForm()
    section_subjects = SectionSubject.objects.all()
    if request.method == 'POST':
        form = forms.SectionSubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add-section-subject')
    context = {
        'form': form,
        'subjects': section_subjects
    }    
    return render(request, 'timetable/add-section-subject.html', context)

@login_required(login_url='login')
def AddTimetableTeacher(request):
    form = forms.AddTeacherForm()
    teachers = Teacher.objects.all().order_by('code')
    if request.method == 'POST':
        form = forms.AddTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add-timetable-teacher')
    context =  {
        'form': form,
        'teachers': teachers
    }
    return render(request, 'timetable/add-teacher.html', context)

@login_required(login_url='login')
def AddClassSubjects(request):
    form = forms.ClassSubjectsForm()
    classes = Class_Subjects.objects.all()
    if request.method == 'POST':
        form = forms.ClassSubjectsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Class Subjects created successfully')
            return redirect('timetable-class-subjects')
    context = {
        'form': form,
        'classes': classes
    }    
    return render(request, 'timetable/add-class-subjects.html', context)

@login_required(login_url='login')
def DeleteClassSubjects(request):
    if request.method == 'POST':
        id = request.POST['id']
        Class_Subjects.objects.get(id=id).delete()
        messages.info(request, 'Class Subjects deleted successdully')
        return redirect('timetable-class-subjects')

@login_required(login_url='login')
def DeleteSectionSubjects(request):
    if request.method == 'POST':
        id = request.POST['id']
        SectionSubject.objects.get(id=id).delete()
        messages.info(request, 'Class Subjects deleted successdully')
        return redirect('add-section-subject')      

