from django.db import models

# Create your models here.

from django.db import models

class Answer(models.Model):
    answA = models.CharField(max_length=1)
    answB = models.CharField(max_length=1)
    answC = models.CharField(max_length=1)
    answCorrect = models.CharField(max_length=1)

# Pomiędzy klasami mają być dwie linijki odstępu. 
class Question(models.Model):
    title = models.CharField(max_length=100)
    answer = models.ForeignKey('Answer', on_delete=models.PROTECT) # W nawiasie podajemy nazwę klasy, do której się odwołujemy.