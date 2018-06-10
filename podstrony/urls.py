from django.urls import path, re_path, include
from django.conf.urls import url
from podstrony.views import ImageDetailView, BudowaDetailView, BudowaListView, TeoriaListView, TeoriaDetailView, PrzepisyListView, PrzepisyDetailView
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [ 
    re_path(r'^budowa/$', BudowaListView.as_view(), name='Budowa-list'),
    re_path(r'^budowa/(?P<pk>\d+)/$', BudowaDetailView.as_view(), name='Budowa-detail'), #powiązanie ścieżki z widokiem i dodanie nazwy, którą można użyć w a href=""
    
    re_path(r'^teoria/$', TeoriaListView.as_view(), name='Teoria-list'),
    re_path(r'^teoria/(?P<pk>\d+)/$', TeoriaDetailView.as_view(), name='Teoria-detail'),

    re_path(r'^przepisy/$', PrzepisyListView.as_view(), name='Przepisy-list'),
    re_path(r'^przepisy/(?P<pk>\d+)/$', PrzepisyDetailView.as_view(), name='Przepisy-detail'),

    re_path(r'^przepisy/(?P<pk>\d+)/$', ImageDetailView.as_view(), name='Image-detail'),

  
    
    
    
    re_path(r'^$', views.index, name='base'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)