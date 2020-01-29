from django.shortcuts import render
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import ProfileForm

def profile(request):
    profile = UserProfile.objects.get(id=request.user.id)
    context = {
        'profile': profile
    }
    return render(request, 'account/profile.html', context)

def update_profile(request):
    profile = UserProfile.objects.get(id=request.user.id)
    forms = ProfileForm(instance=profile)
    if request.method == 'POST':
        forms = ProfileForm(request.POST, request.FILES, instance=profile)
        if forms.is_valid():
            forms.save()
    context = {
        'forms': forms
    }
    return render(request, 'account/update-profile.html', context)
