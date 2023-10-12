from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):  # Отображение заголовков в панели администратора
        return self.title
