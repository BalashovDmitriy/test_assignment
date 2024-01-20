from django.contrib import admin

from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_active', 'is_staff']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
    )


admin.site.register(User, UserAdmin)
