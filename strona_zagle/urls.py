from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    re_path(r'^shelf/', include('shelf.urls',)),# Jeśli w linku zostanie wyłapane
                                                            # wszystko zaczynające się od shelf/
                                                            #Każdą linijkę (re_path) w shelf.urls zacznie od ^shelf/
    re_path(r'', include('shelf.urls',)),
    re_path(r'', include('podstrony.urls',)),
    url(r'^accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
