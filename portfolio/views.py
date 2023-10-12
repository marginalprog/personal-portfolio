from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all()  # Импорт всех записей о проектах из БД
    return render(request, "portfolio/home.html", {"projects": projects})
