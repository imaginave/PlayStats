
# Register your models here.

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from stats.models import Transations
from django.contrib import admin
from .models import Transations
from import_export.admin import ImportExportModelAdmin


@admin.register(Transations)
class PersonAdmin(ImportExportModelAdmin):
    pass



