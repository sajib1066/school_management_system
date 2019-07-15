from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from teacher.models import Department, Designation, District, Upazilla, Union
from .forms import *

def admin_login(request):
    forms = AdminLoginForm()
    if request.method == 'POST':
        forms = AdminLoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    context = {'forms': forms}
    return render(request, 'administration/login.html', context)

def admin_logout(request):
    logout(request)
    return redirect('home')


def add_designation(request):
    forms = AddDesignationForm()
    if request.method == 'POST':
        forms = AddDesignationForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('designation')
    designation = Designation.objects.all()
    context = {'forms': forms, 'designation': designation}
    return render(request, 'administration/designation.html', context)

def load_upazilla(request):
    district_id = request.GET.get('district')
    print('....................')
    print(district_id)
    upazilla = Upazilla.objects.filter(district_id=district_id).order_by('name')
    context = {
        'upazilla': upazilla
    }
    return render(request, 'administration/upazilla_dropdown_list_options.html', context)

def load_union(request):
    upazilla_id = request.GET.get('upazilla')
    union = Union.objects.filter(upazilla_id=upazilla_id).order_by('name')
    context = {
        'union': union
    }
    return render(request, 'others/union_dropdown_list_options.html', context)


def add_district(request):
    forms = DistrictForm()
    if request.method == 'POST':
        forms = DistrictForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('district')
    district = District.objects.all()
    context = {'forms': forms, 'district': district}
    return render(request, 'administration/district.html', context)

def add_upazilla(request):
    forms = UpazillaForm()
    if request.method == 'POST':
        forms = UpazillaForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('upazilla')
    upazilla = Upazilla.objects.all()
    context = {'forms': forms, 'upazilla': upazilla}
    return render(request, 'administration/upazilla.html', context)

def add_union(request):
    forms = UnionForm()
    if request.method == 'POST':
        forms = UnionForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('union')
    union = Union.objects.all()
    context = {'forms': forms, 'union': union}
    return render(request, 'administration/union.html', context)
