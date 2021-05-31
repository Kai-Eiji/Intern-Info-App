from django.contrib import admin
from .models import Interns

class InternsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Interns, InternsAdmin)

