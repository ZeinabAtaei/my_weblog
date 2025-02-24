from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import CustomUserChangeForm, CustomUserCreationForm
from accounts.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    fieldsets = UserAdmin.fieldsets +(
        (None, {'fields': ('age', )}),
    )

    add_fieldsets = UserAdmin.add_fieldsets +(
        (None, {'fields': ('age', )}),
    )

admin.site.register(CustomUser, CustomUserAdmin)