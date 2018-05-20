from django.db import models

# Create your models here.

from django.db import models

class Answer(models.Model):
    answA = models.CharField(max_length=20)
    answB = models.CharField(max_length=20)
    answC = models.CharField(max_length=20)
    answCorrect = models.CharField(max_length=1)

    def __str__(self): #metoda, która wyświetla napis obiektu
        return "A={answA}; B={answB}; C={answC}; Answer={answCorrect}".format(answA=self.answA, answB=self.answB, answC=self.answC, answCorrect=self.answCorrect)

# Pomiędzy klasami mają być dwie linijki odstępu. 
class Question(models.Model):
    title = models.CharField(max_length=100)
    answer = models.ForeignKey('Answer', on_delete=models.PROTECT) # W nawiasie podajemy nazwę klasy, do której się odwołujemy.

    def __str__(self): #metoda, która wyświetla napis obiektu
        return self.title