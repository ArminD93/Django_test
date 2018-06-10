from django.contrib import admin
#Importowanie z modeli
from .models import Teoria, Budowa, Reporter, Przepisy, Image # Nigdy nie robić import * w Python!!
# Register your models here.


class BudowaAdmin(admin.ModelAdmin):#klasa administracyjna dla Question, 
    search_fields = ['headline']
    list_display = ['headline', 'pub_date', 'content']
    ordering = ['headline' ]


class TeoriaAdmin(admin.ModelAdmin):#klasa administracyjna dla Question, 
    search_fields = ['headline']
    list_display = ['headline', 'pub_date', 'content']
    ordering = ['headline' ]


class PrzepisyAdmin(admin.ModelAdmin):#klasa administracyjna dla Question, 
    search_fields = ['headline']
    list_display = ['headline', 'pub_date', 'content']
    ordering = ['headline' ]


class ImageAdmin(admin.ModelAdmin):#klasa administracyjna dla Question, 
    search_fields = ['headline']
    list_display = ['headline', 'pub_date', 'article', 'img']
    ordering = ['headline' ]


class ReporterAdmin(admin.ModelAdmin):
    search_fields = ['full_name']
    list_display = ['full_name']
    ordering = ['full_name' ]


admin.site.register(Budowa, BudowaAdmin)
admin.site.register(Teoria, TeoriaAdmin)
admin.site.register(Przepisy, PrzepisyAdmin)
admin.site.register(Reporter, ReporterAdmin)
admin.site.register(Image, ImageAdmin)