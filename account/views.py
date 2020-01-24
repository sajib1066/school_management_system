from django.shortcuts import render
from django.contrib.auth.models import User
from .models import UserProfile

def profile(request):
    profile = UserProfile.objects.get(id=request.user.id)
    context = {
        'profile': profile
    }
    return render(request, 'account/profile.html', context)
