from django.shortcuts import render

# Create your views here.
from .models import Project

#
# def projects(request):
#     return render(request,'projects/projects.html',{})

def project_index(request):
    projects = Project.objects.all()
    context  = {
        'projects':projects
    }
    return render(request,'projects/project_index.html',context)

def project_details(request,pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project':project
    }
    return render(request,'projects/project_detail.html',context)

