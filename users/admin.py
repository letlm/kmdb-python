from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUserAdmin(UserAdmin):

    readonly_fields = ("updated_at", "date_joined", "last_login")

    fieldsets = (
        ("Credentials", {"fields": ("username", "password")}),
        ("Personal Info", {"fields": ("email", "bio", "birthdate")}),
        ("Permissions", {"fields": ("is_superuser", "is_critic")}),
        ("Important Dates", {"fields": ("updated_at", "date_joined", "last_login")}),
    )


admin.site.register(User, CustomUserAdmin)
