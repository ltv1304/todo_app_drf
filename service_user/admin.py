from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import ServiceUser


@admin.register(ServiceUser)
class ServiceUserAdmin(UserAdmin):

    model = ServiceUser

    list_display = ['username', 'first_name', 'last_name', 'email', 'is_staff']

    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'groups',
                )
            }
        )
    )



# Register your models here.
