from django.db import models
class Author(models.Model):
    firstname = models.CharField(max_length=255, blank=False)
    lastname = models.CharField(max_length=255, blank=False)
    wikipedia = models.CharField(max_length=255, blank=False)
    def __str__(self):
        return self.firstname+self.lastname

    
class Book (models.Model):
    
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    summary = models.TextField(blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    Aventure = 'Av'
    Thriller = 'Th'
    Fantastique = 'Fa'
    Romance = 'Ro'
    Horreur = 'Ho'
    Sciencefiction = 'Sf'
    category_choices = [
                (Aventure,'Aventure'),
                (Thriller,'Thriller'),
                (Fantastique,'Fantastique'),
                (Romance,'Romance'),
                (Horreur,'Horreur'),
                (Sciencefiction,'Science-fiction')]
    category = models.CharField(max_length=2,
                                choices = category_choices,
                                default=Aventure)
    def __str__(self):
        return self.title