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
        subjects = list(SubjectRegistration.objects.filter(select_class=classs))
        class_periods = list(Period.objects.filter(section=classs.section))
        break_time = Breaks.objects.get(section=classs.section)
        if Timetable.objects.filter(school_class__id=idf).count() != 0:
            Timetable.objects.filter(school_class__id=idf).delete()
        for subject in subjects:
            DupNum = 0
            y = 0
            if DupNum > len(class_periods):
                messages.info(request, "Couldn't create Timetable")
                return
            while y < subject.periods_per_week:
                if DupNum > len(class_periods):
                    break
                i = random.randint(0, len(class_periods)-1)
                start_conflict = Timetable.objects.filter(period__day=class_periods[i].day,
                    period__start_time__range=(class_periods[i].start_time,
                                    class_periods[i].end_time))
                end_conflict = Timetable.objects.filter(period__day=class_periods[i].day,
                period__end_time__range=(class_periods[i].start_time,
                                class_periods[i].end_time))

                during_conflict = Timetable.objects.filter(period__day=class_periods[i].day,
                    period__start_time__gte=class_periods[i].start_time, 
                    period__end_time__lte=class_periods[i].end_time)
                if start_conflict.count() == 0 and end_conflict.count() == 0 and during_conflict.count() == 0:
                    Timetable.objects.create(school_class=classs, subject=subject, period=class_periods[i])
                    DupNum = 0
                    y+=1
                else:
                    DupNum += 1    

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
