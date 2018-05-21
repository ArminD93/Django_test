from django.urls import path, re_path, include
from shelf.views import Question_MeteoListView, Question_MeteoDetailView

urlpatterns = [ 
    re_path(r'^meteo/$', Question_MeteoListView.as_view(), name='Question_Meteo-list'),
    re_path(r'^meteo/(?P<pk>\d+)/$', Question_MeteoDetailView.as_view(), name='Question_Meteo-detail'), #powiązanie ścieżki z widokiem i dodanie nazwy, którą można użyć w a href=""
]