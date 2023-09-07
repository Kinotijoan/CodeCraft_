from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        'email',
        'first_name',
        'last_name',
        'username',
        'projects',
        'is_staff',
        'is_active',
    )
    list_filter = (
        'email',
        'is_staff',
        'is_active',
    )
    fieldsets = (
        (None, {'fields': ('username', 'first_name', 'last_name', 'projects', 'email', 'password')}),
        (
            'Permissions',
            {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'username',
                    'first_name',
                    'last_name',
                    'email',
                    'projects',
                    'password1',
                    'password2',
                    'is_staff',
                    'is_active',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
