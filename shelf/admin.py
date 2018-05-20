from django.contrib import admin
#Importowanie z modeli
from .models import Question_Meteo, Answer_Meteo # Nigdy nie robić import * w Python!!
# Register your models here.


class Question_MeteoAdmin(admin.ModelAdmin):#klasa administracyjna dla Question, 
    search_fields = ['title']
    list_display = ['title', 'answA', 'answB', 'answC', 'answCorrect']
    ordering = ['title' ]


admin.site.register(Question_Meteo, Question_MeteoAdmin)
#admin.site.register([Question_Meteo, Answer_Meteo])