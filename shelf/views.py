from django.shortcuts import render
from django.views.generic import ListView, DetailView #Zawiera widoki generyczne, które zostały przygotowane przez twórców Django do obsługi najpopularniejszych obiektów

from .models import Question_Meteo # Jeśli importujemy coś z submodułu, to odwołujemy się do kropki.
# Create your views here.

class Question_MeteoListView(ListView):
    model = Question_Meteo

class Question_MeteoDetailView(DetailView):
    model = Question_Meteo

def index(request):
    return render(request, template_name="base.html")