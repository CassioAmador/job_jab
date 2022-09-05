from django.contrib import admin

from .models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ("doc_id", "employer_name", "date_posted", "employment_type", "location", "title", "description")

admin.site.register(Job, JobAdmin)