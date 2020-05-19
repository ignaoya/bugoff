from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Project, Bug, Worknote


def index(request):
    return HttpResponse("Welcome to Bugoff! The online Python bug tracker.")

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'tracker/project/list.html', {'projects': projects})

def project_detail(request, name):
    project = get_object_or_404(Project, name=name)
    return render(request, 'tracker/project/detail.html', {'project': project})

def bug_detail(request, id):
    bug = get_object_or_404(Bug, id=id)
    return render(request, 'tracker/bug/detail.html', {'bug': bug})

