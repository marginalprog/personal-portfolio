from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="portfolio/images/", max_length=250)
    url = models.URLField(blank=True)

    def __str__(self):  # Отображение заголовков в панели администратора
        return self.title
