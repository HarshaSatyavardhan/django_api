from os import system
from django.db import models

class Researchpaper(models.Model):
    title = models.CharField(max_length=250, null=True)
    publication = models.CharField(max_length=250, null=True)
    link = models.URLField(max_length=500, null=True, blank=True)
    authors = models.CharField(max_length=200, null=True)
    year = models.IntegerField(null=True,blank=True)
    abstract = models.TextField(max_length=5000, null=True)

    methodology = models.TextField(max_length=5000, null=True)
    methodology_two = models.TextField(max_length=5000, null=True,blank=True)
    methodology_three = models.TextField(max_length=5000, null=True,blank=True)
    methodology_four = models.TextField(max_length=5000, null=True,blank=True)
    methodology_five = models.TextField(max_length=5000, null=True,blank=True)


    result = models.TextField(max_length=5000, null=True,blank=True)
    result_two = models.TextField(max_length=5000, null=True,blank=True)
    result_three = models.TextField(max_length=5000, null=True,blank=True)
    result_four = models.TextField(max_length=5000, null=True,blank=True)
    result_five = models.TextField(max_length=5000, null=True,blank=True)

    discussion = models.TextField(max_length=5000, null=True,blank=True)
    codes = models.TextField(max_length=5000, null=True,blank=True)
    system = models.TextField(max_length=5000, null=True,blank=True)

    def __str__(self) :
        return self.title



class People(models.Model):
    #image = models.ImageField(max_length=None, allow_empty_file=True)
    Name = models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=50, null=True)
    google_scholar = models.URLField(max_length=500, null=True)
    twitter = models.URLField(max_length=500, null=True)
    linkedin = models.URLField(max_length=500, null=True)

    def __str__(self):
        return self.Name