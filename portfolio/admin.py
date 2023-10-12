from django.contrib import admin
from .models import Project  # Импорт в админку модели(класса) Project

admin.site.register(Project)

