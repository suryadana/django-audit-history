from django.contrib import admin
from audit_history.models import (
    AuditRequest, AuditException, AuditResponse
)

# Register your models here.


class AuditRequestAdmin(admin.ModelAdmin):
    list_display = ('ip', 'url', 'user', 'time')


class AuditExceptionAdmin(admin.ModelAdmin):
    list_display = ('request', 'time')


class AuditResponseAdmin(admin.ModelAdmin):
    list_display = ('request', 'time')


admin.site.register(AuditRequest, AuditRequestAdmin)
admin.site.register(AuditException, AuditExceptionAdmin)
admin.site.register(AuditResponse, AuditResponseAdmin)
