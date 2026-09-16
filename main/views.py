from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.core import serializers
from main.forms import ProjectForm
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

def create_project(request):
    form = ProjectForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")
    context = {
        "name": "Fildza Hasnalia Nabila",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()
    if title_query:
        projects = projects.filter(title__icontains=title_query)
    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def show_projects(request):
    json_response = get_projects_json(request)
    projects = serializers.deserialize("json", json_response.content.decode("utf-8"))
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()
    context = {
        "name": "Fildza Hasnalia Nabila",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")
    return redirect("main:show_projects")