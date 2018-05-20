from django.db import models

# Create your models here.

from django.db import models

class Answer_Meteo(models.Model):
    id = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=100, default='SOME STRING')
    answA = models.CharField(max_length=100)
    answB = models.CharField(max_length=100)
    answC = models.CharField(max_length=100)
    answCorrect = models.CharField(max_length=1)

    def __str__(self): #metoda, która wyświetla napis obiektu
        #return "A={answA}; B={answB}; C={answC}; Answer={answCorrect}".format(answA=self.answA, answB=self.answB, answC=self.answC, answCorrect=self.answCorrect)
        return self.name


# Pomiędzy klasami mają być dwie linijki odstępu. 
class Question_Meteo(models.Model):
    title = models.CharField(max_length=100)
    #answer = models.ForeignKey('Answer_Meteo', on_delete=models.PROTECT) # W nawiasie podajemy nazwę klasy, do której się odwołujemy.
    answA = models.CharField(max_length=100)
    answB = models.CharField(max_length=100)
    answC = models.CharField(max_length=100)
    answCorrect = models.CharField(max_length=1)

    def __str__(self): #metoda, która wyświetla napis obiektu
        return self.title