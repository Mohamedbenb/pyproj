from django.db import models

# Create your models here.

class Author(models.Model):
    firstname = models.CharField(max_length=255, blank=False)
    lastname = models.CharField(max_length=255, blank=False)
    wikipedia = models.CharField(max_length=255, blank=False)
    def __str__(self):
        return self.firstname+self.lastname

class BlogPost (models.Model):
        
    title = models.CharField(max_length=255)
    author = models.TextField(blank=True)
    content = models.TextField(blank=True)
    created_on = models.TextField(blank=True)
    def __str__(self):
        return self.title