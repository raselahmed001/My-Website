from django.contrib import admin
from .models import *


# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name", "position", "location"]
    search_fields = ["position", "name", "location", "salary"]
    list_filter = ["salary"]


class CandidateAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]
    search_fields = ["name", "email", "company"]
    list_filter = ["name"]


admin.site.register(Company, CompanyAdmin)
admin.site.register(Candidate, CandidateAdmin)
