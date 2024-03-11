from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255, blank=False)
    create_data = models.DateField(blank=False)
    summary = models.TextField(max_length=200, blank=False)
    publisher = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, blank=False)
    birth_date = models.DateField(blank=False)

    def __str__(self):
        return self.name
