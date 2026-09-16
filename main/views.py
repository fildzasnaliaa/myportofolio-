from django.shortcuts import render
from main.models import Experience, Project

def show_main(request):
    experiences = Experience.objects.all()
    context = {
        'npm': '2506625003',
        'name': 'Fildza Hasnalia Nabila',
        'class': 'PBP A',
        'experiences': experiences
    }
    return render(request, "index.html", context)

def show_experience(request):
    experiences = Experience.objects.all()
    context = {
        'name': 'Fildza Hasnalia Nabila',
        'experiences': experiences
    }
    return render(request, "experience.html", context)

def show_project(request):
    projects = Project.objects.all()
    context = {
        'name': 'Fildza Hasnalia Nabila',
        'projects': projects
    }
    return render(request, "projects.html", context)