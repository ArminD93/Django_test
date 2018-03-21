from django.contrib import admin
#Importowanie z modeli
from .models import Question, Answer # Nigdy nie robić import * w Python!!
# Register your models here.

admin.site.register([Question, Answer])