from django.contrib import admin

from users.models import User


class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff')
        }),
    )
    list_display = ('email', 'is_active', 'is_staff')


admin.site.register(User, UserAdmin)
