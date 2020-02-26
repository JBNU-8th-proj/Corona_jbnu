from django.contrib import admin
from . import models

@admin.register(models.Patient)
class PatientAdmin(admin.ModelAdmin):

    """Patient Admin Definition"""
    list_display = (
        "patient_index",
        "status",
        "latitude",
        "longitude",
    )

    list_filter = (
        "patient_index",
    )