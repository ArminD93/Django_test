from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Strona_ZagleUser
from django.utils.translation import ugettext_lazy as _


# Register your models here.

class Strona_ZagleUserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('myuser1_field', 'first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Additional info'), {'fields': ('avatar', 'phone')}),
    )


admin.site.register(Strona_ZagleUser, Strona_ZagleUserAdmin)

