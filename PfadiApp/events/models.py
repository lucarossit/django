from django.db import models

class Event(models.Model):
    title = models.TextField()
    date = models.DateField()
    def __str__(self):
        return f'{self.title}'

class Participant(models.Model):
    name = models.TextField()
    email = models.EmailField()
    event = models.ManyToManyField(Event)
