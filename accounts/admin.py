from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, Driver, Admin

# Custom admin class to control how CustomUser is displayed
class CustomUserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = ('email', 'full_name', 'role', 'is_staff', 'is_superuser')
    list_filter = ('role', 'is_staff', 'is_superuser')

    fieldsets = (
        #basic login info
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('full_name', 'phone', 'role')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}),
        ('Import dates', {'fields': ('last_login', 'date_joined')}),
    )


    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'phone', 'role', 'password1' 'password2' 'is_staff', 'is_superuser'),

        }),
    )

#fields that can be searched in the admin interface
    search_fields  = ('email', 'full_name')

    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Driver)
admin.site.register(Admin)