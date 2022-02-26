from django.contrib import admin
from .models import ServiceUser


class ServiceUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')


admin.site.register(ServiceUser, ServiceUserAdmin)


# Register your models here.
