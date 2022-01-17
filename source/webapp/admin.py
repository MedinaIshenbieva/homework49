from django.contrib import admin

from webapp.models import Task, Status, Type


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'status']
    list_filter = ['status', 'type']
    search_fields = ['summary', 'status', 'type']
    fields = ['summary', 'description', 'status', 'type']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Task, TaskAdmin)
admin.site.register(Status)
admin.site.register(Type)

