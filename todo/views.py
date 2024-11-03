from django.shortcuts import render

from todo.models import Item, Project


def project_list(request):

    list = Project.objects.all()

    return render(request, "todo_list.html", {"list": list})
