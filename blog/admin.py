from django.contrib import admin
from .models import Blog  # Импорт в админку модели(класса) Post

admin.site.register(Blog)
