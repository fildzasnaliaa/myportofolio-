from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from main.models import Project, Experience
from main.forms import ProjectForm, ExperienceForm

def show_main(request):
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    context = {
        'projects': projects,
        'experiences': experiences,
    }
    return render(request, 'index.html', context)

def show_education(request):
    return render(request, 'education.html')

def show_projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects.html', context)

def show_experience(request):
    experiences = Experience.objects.all()
    context = {'experiences': experiences}
    return render(request, 'experience.html', context)

def show_experience_json(request):
    data = Experience.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def create_experience(request):
    form = ExperienceForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_experience')
    context = {'form': form}
    return render(request, 'create_experience.html', context)

def update_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    form = ExperienceForm(request.POST or None, instance=experience)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_experience')
    context = {'form': form}
    return render(request, 'update_experience.html', context)

def delete_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    experience.delete()
    return redirect('main:show_experience')

def create_project(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_projects')
    context = {'form': form}
    return render(request, 'projects_form.html', context)

def update_project(request, id):
    project = get_object_or_404(Project, pk=id)
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_projects')
    context = {'form': form}
    return render(request, 'projects_form.html', context)

def delete_project(request, id):
    project = get_object_or_404(Project, pk=id)
    project.delete()
    return redirect('main:show_projects')