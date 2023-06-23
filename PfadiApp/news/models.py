from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    title = models.TextField()
    description = models.TextField()
    date = models.DateField()