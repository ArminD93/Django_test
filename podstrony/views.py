from django.shortcuts import render
from django.views.generic import ListView, DetailView #Zawiera widoki generyczne, które zostały przygotowane przez twórców Django do obsługi najpopularniejszych obiektów

from .models import Budowa # Jeśli importujemy coś z submodułu, to odwołujemy się do kropki.
# Create your views here.



class BudowaDetailView(DetailView):
    model = Budowa


class BudowaListView(ListView):
    model = Budowa


def index(request):
    return render(request, template_name="base.html")

