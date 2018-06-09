from django.urls import path, re_path, include
from django.conf.urls import url
from podstrony.views import BudowaDetailView, BudowaListView
from . import views

'''
urlpatterns = [
    url(r'^$', views.Budowa_list, name='Budowa_list'),
    url(r'^budowa/(?P<pk>\d+)/$', views.Budowa_detail, name='Budowa_detail'),
    
    re_path(r'^budowa/$', BudowaDetailView.as_view(), name='Budowa-detail'),
]   
'''

urlpatterns = [ 
    re_path(r'^budowa/$', BudowaListView.as_view(), name='Budowa-list'),
    re_path(r'^budowa/(?P<pk>\d+)/$', BudowaDetailView.as_view(), name='Budowa-detail'), #powiązanie ścieżki z widokiem i dodanie nazwy, którą można użyć w a href=""
    re_path(r'^$', views.index, name='base'),
]