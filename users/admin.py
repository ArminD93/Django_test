from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import StronaZagleUser
from django.utils.translation import ugettext_lazy as _


# Register your models here.

class StronaZagleUserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Additional info'), {'fields': ('avatar', 'phone')}),
    )


admin.site.register(StronaZagleUser, StronaZagleUserAdmin)


