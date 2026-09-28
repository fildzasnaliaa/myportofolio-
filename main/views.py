import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.models import Project, Experience
from main.forms import ProjectForm, ExperienceForm

def show_main(request):
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    context = {
        'projects': projects,
        'experiences': experiences,
        'last_login': request.COOKIES.get('last_login', 'Belum pernah login'),
    }
    return render(request, 'index.html', context)

def show_education(request):
    return render(request, 'education.html')

def show_projects(request):
    projects = Project.objects.all()
    # Mengecek apakah user yang sedang login merupakan anggota grup Editor
    is_editor = request.user.is_authenticated and request.user.groups.filter(name='Editor').exists()
    context = {
        'projects': projects,
        'is_editor': is_editor,
    }
    return render(request, 'projects.html', context)

def show_experience(request):
    experiences = Experience.objects.all()
    context = {'experiences': experiences}
    return render(request, 'experience.html', context)

def show_experience_json(request):
    data = Experience.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login/')
def create_experience(request):
    if not (request.user.is_superuser):
        return HttpResponseForbidden("Hanya superuser yang dapat membuat data experience.")
    form = ExperienceForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        experience = form.save(commit=False)
        experience.user = request.user
        experience.save()
        return redirect('main:show_experience')
    context = {'form': form}
    return render(request, 'create_experience.html', context)

@login_required(login_url='/login/')
def update_experience(request, id):
    is_editor = request.user.groups.filter(name='Editor').exists()
    if not (request.user.is_superuser or is_editor):
        return HttpResponseForbidden("Anda tidak memiliki hak akses untuk mengubah data ini[cite: 5].")
    experience = get_object_or_404(Experience, pk=id)
    form = ExperienceForm(request.POST or None, instance=experience)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_experience')
    context = {'form': form}
    return render(request, 'update_experience.html', context)

@login_required(login_url='/login/')
def delete_experience(request, id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Hanya superuser yang dapat menghapus data.")
    experience = get_object_or_404(Experience, pk=id)
    experience.delete()
    return redirect('main:show_experience')

@login_required(login_url='/login/')
def create_project(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Hanya pemilik portofolio (superuser) yang dapat membuat project[cite: 5].")
    form = ProjectForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        project = form.save(commit=False)
        project.user = request.user
        project.save()
        return redirect('main:show_projects')
    context = {'form': form}
    return render(request, 'projects_form.html', context)

@login_required(login_url='/login/')
def update_project(request, id):
    is_editor = request.user.groups.filter(name='Editor').exists()
    if not (request.user.is_superuser or is_editor):
        return HttpResponseForbidden("Anda tidak memiliki hak akses untuk mengubah project ini[cite: 5].")
    project = get_object_or_404(Project, pk=id)
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_projects')
    context = {'form': form}
    return render(request, 'projects_form.html', context)

@login_required(login_url='/login/')
def delete_project(request, id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Hanya pemilik portofolio (superuser) yang dapat menghapus project[cite: 5].")
    project = get_object_or_404(Project, pk=id)
    project.delete()
    return redirect('main:show_projects')

@login_required(login_url='/login/')
def toggle_star(request, id):
    project = get_object_or_404(Project, pk=id)
    if project.starred_by.filter(id=request.user.id).exists():
        project.starred_by.remove(request.user)
    else:
        project.starred_by.add(request.user)
    return redirect('main:show_projects')

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun berhasil dibuat!')
            return redirect('main:login')
    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse('main:show_main'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response