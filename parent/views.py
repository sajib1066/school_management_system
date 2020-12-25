from django.shortcuts import render, redirect
from django.contrib import messages
from student.models import AcademicInfo, PersonalInfo

# Create your views here.
def child_info(request):
    try:
        children = AcademicInfo.objects.filter(guardian_info__login_details=request.user
        context = {
            'children': children
        }
        return render(request, 'parent/student-profile.html')
    except:
        messages.error(request, 'Could not get child info. Please contact admin')    
        return redirect('home')