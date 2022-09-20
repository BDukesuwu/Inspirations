from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date


# Create your models here please


class Gallery(models.Model):  # IS A
    name = models.CharField(max_length=100)  # HAS A
    description = models.TextField(max_length=250)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.description}"

    def get_absolute_url(self):
        return reverse('galleries_detail', kwargs={'pk': self.id})

class Inspiration(models.Model):
    name = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)

    galleries = models.ManyToManyField(Gallery)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('inspirations_detail', kwargs={'pk': self.id})

class Note(models.Model):
    date = models.DateField()
    note = models.TextField(max_length=1000)

    inspiration = models.ForeignKey(Inspiration, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.note} {self.date}"

    class Meta:
        ordering = ['-date']