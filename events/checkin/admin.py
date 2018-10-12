from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Guest


@admin.register(Guest)
class ViewAdmin(ImportExportModelAdmin):
    pass
