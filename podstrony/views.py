from django.shortcuts import render
from django.views.generic import ListView, DetailView #Zawiera widoki generyczne, które zostały przygotowane przez twórców Django do obsługi najpopularniejszych obiektów

from .models import Budowa, Teoria, Przepisy, Image # Jeśli importujemy coś z submodułu, to odwołujemy się do kropki.
# Create your views here.



class BudowaDetailView(DetailView):
    model = Budowa


class BudowaListView(ListView):
    model = Budowa

################################################

class TeoriaDetailView(DetailView):
    model = Teoria


class TeoriaListView(ListView):
    model = Teoria

################################################

class PrzepisyDetailView(DetailView):
    model = Przepisy


class PrzepisyListView(ListView):
    model = Przepisy

################################################

class ImageDetailView(DetailView):
    model = Image


class ImageListView(ListView):
    model = Image


def index(request):
    return render(request, template_name="base.html")




