from django.contrib import admin

from notes.models import Project, TODO


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'path')


class TODOAdmin(admin.ModelAdmin):
    list_display = ('project', 'user', 'published', 'updated', 'active_flag')


admin.site.register(Project, ProjectAdmin)
admin.site.register(TODO, TODOAdmin)
