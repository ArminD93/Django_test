from django.contrib import admin
#Importowanie z modeli
from .models import Budowa, Reporter # Nigdy nie robić import * w Python!!
# Register your models here.


class BudowaAdmin(admin.ModelAdmin):#klasa administracyjna dla Question, 
    search_fields = ['headline']
    list_display = ['headline', 'pub_date', 'content']
    ordering = ['headline' ]

class ReporterAdmin(admin.ModelAdmin):
    search_fields = ['full_name']
    list_display = ['full_name']
    ordering = ['full_name' ]


admin.site.register(Budowa, BudowaAdmin)
admin.site.register(Reporter, ReporterAdmin)