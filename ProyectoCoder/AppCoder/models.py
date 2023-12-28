from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=60)
    year=models.IntegerField()
    author=models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.title} | {self.year} | {self.author}"


class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age=models.IntegerField()
    publications=models.TextField()
    
    def __str__(self):
       return f"{self.name} | {self.surname} | {self.age} | {self.publications}"
    

class Journal(models.Model):
    title = models.CharField(max_length=60)
    year=models.IntegerField()
    author=models.CharField(max_length=30)
    keywords=models.TextField()
    
    def __str__(self):
        return f"{self.title} | {self.year} | {self.author} | {self.keywords}"


class Publication(models.Model):
    name= models.CharField(max_length=60)
    author=models.CharField(max_length=30)
    isActive = models.BooleanField()
    
    def __str__(self):
        return f"{self.name} | {self.author} | {self.isActive}"