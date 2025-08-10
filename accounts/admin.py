from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, Driver, Admin
from rides.models import Journey


#Inline display of journeys of each driver 
class JourneyInline(admin.TabularInline):
    model = Journey
    extra = 0
    fields = ('origin', 'destination', 'vehicle', 'departure_time', 'price')
    readonly_fields = ('origin', 'destination', 'vehicle', 'departure_time', 'price')

class DriverAdmin(admin.ModelAdmin):
    """ Custom admin view for the driver model.
    shows driver details and their assigned journeys.
    """
    list_display = ('user', 'license_number', 'national_id')
    search_fields = ('user__full_name', 'license_number', 'national_id')
    inlines = [JourneyInline] #attach the journey list inside the driver detail page

# Custom admin class for CustomUser
class CustomUserAdmin(BaseUserAdmin): 
    model = CustomUser
    list_display = ('email', 'full_name', 'role', 'is_staff', 'is_superuser')
    list_filter = ('role', 'is_staff', 'is_superuser')

    fieldsets = (
        #basic login info, personal details, permissions & groups and dates
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
admin.site.register(Driver, DriverAdmin)
admin.site.register(Admin)