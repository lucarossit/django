from django.db import models

class News(models.Model):
    title = models.TextField()
    description = models.TextField()
    date = models.DateField()