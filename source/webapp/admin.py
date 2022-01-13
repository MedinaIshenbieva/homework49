from django.contrib import admin

from webapp.models import IssueTracker, Status, Type


class IssueTrackerAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'status', 'type']
    list_filter = ['status', 'type']
    search_fields = ['summary', 'status', 'type']
    fields = ['summary', 'description', 'status', 'type']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(IssueTracker, IssueTrackerAdmin)
admin.site.register(Status)
admin.site.register(Type)

