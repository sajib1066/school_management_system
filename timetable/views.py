from django.shortcuts import render, redirect
from academic.models import ClassRegistration
from result.models import SubjectRegistration
from .models import *
from . import forms
from django.contrib import messages
import random

# Create your views here.
def AddPeriod(request):
    try:
        time = Period.objects.all()
    except:
        time = None 
    breakform = forms.BreakForm()           
    form = forms.PeriodForm()
    if request.method == 'POST':
        try:
            form = forms.PeriodForm(request.POST)
            form.save()
            messages.info(request, 'Form saved successfully')
        except:
            messages.info(request, "Couldn't save form")    
    context = {
        'form': form,
        'periods': time,
        'breakform': breakform
    }
    return render(request, 'timetable/add-period.html', context)

def GenerateTimetable(request):
    if request.method == 'POST':
        idf = request.POST["timetable_class_id"]
        classs = ClassRegistration.objects.get(id=idf)
        subjects = list(Class_Subjects.objects.filter(subject__select_class=classs))
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        class_periods = list(Period.objects.filter(section=classs.section).order_by('start_time'))
        break_time = Breaks.objects.get(section=classs.section)
        before_break = Period.objects.filter(start_time__lte=break_time.start_time).count()
        if Timetable.objects.filter(school_class__id=idf).count() != 0:
            Timetable.objects.filter(school_class__id=idf).delete()
        for subject in subjects:
            DupNum = 0
            y = 0
            m = 0
            j = 0
            d = 0
            if DupNum > len(class_periods):
                messages.info(request, "Couldn't create Timetable")
                redirect('home')
            while y < subject.no_of_times_a_week:
                if DupNum > len(class_periods) * 5:
                    break
                else:
                    if DupNum < 3:
                        if subject.is_morning and m < 3:
                            i = random.randint(0, before_break)                   
                        else:
                            i = random.randint(0, len(class_periods)-1)
                        d = random.randint(0, len(days)-1)    
                    else:
                        if j <= len(class_periods):
                            if j == len(class_periods) and d < (len(days) - 1):
                                d += 1
                                j = 0
                            elif j < len(class_periods):
                                i = j
                                j += 1
                start_conflict = Timetable.objects.filter(day=days[d],
                    period__start_time__range=(class_periods[i].start_time,
                                    class_periods[i].end_time))
                end_conflict = Timetable.objects.filter(day=days[d],
                period__end_time__range=(class_periods[i].start_time,
                                class_periods[i].end_time))

                during_conflict = Timetable.objects.filter(day=days[d],
                    period__start_time__gte=class_periods[i].start_time, 
                    period__end_time__lte=class_periods[i].end_time)

                teacher_conflict = Timetable.objects.filter(day=days[d], subject__teacher=subject.teacher,
                        period__start_time__gte=class_periods[i].start_time,
                        period__end_time__lte=class_periods[i].end_time)

                subject_conflict = Timetable.objects.filter(day=days[d], subject__subject=subject.subject)

                if start_conflict.count() == 0 and end_conflict.count() == 0 and during_conflict.count() == 0 and teacher_conflict.count() == 0 and subject_conflict.count() == 0:
                    Timetable.objects.create(school_class=classs, subject=subject, period=class_periods[i], day=days[d])
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


def timetable_class_list(request):
    try:
        register_class = ClassRegistration.objects.all()
    except:
        messages.info(request, 'No current classes')
        redirect('home')    
    context = {'register_class': register_class}
    return render(request, 'timetable/time_class-list.html', context)


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

def Edit_Timetable(request, id):
    if request.method == 'POST':
        form = forms.TimetableForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            day = form.cleaned_data['day']
            period = form.cleaned_data['period']
            start_confilct = Timetable.objects.filter(subject__teacher=subject.teacher, day=day, period__start_time__range=(period.start_time, period.end_time))
            end_confilct = Timetable.objects.filter(subject=subject, day=day, period__end_time__range=(period.start_time, period.end_time))
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