from django.shortcuts import render

from project.models import Project


# Create your views here.


def show_projects(request):
    total_projects = Project.objects.all()

    context = {
        'projects': total_projects
    }

    return render(request, 'projects.html', context)
