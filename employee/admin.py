from django.contrib import admin
from .models import ContEmpMast

class ContEmpMastAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ContEmpMast._meta.fields]

admin.site.register(ContEmpMast, ContEmpMastAdmin)
