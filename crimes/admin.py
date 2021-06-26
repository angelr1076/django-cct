from django.contrib import admin
from .models import Crime

class CrimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'crime_type', 'zipcode', 'suspect', 'is_active')
    list_display_links = ('id', 'crime_type')
    list_filter = ('suspect', 'crime_type')
    list_editable = ('is_active',)
    
admin.site.register(Crime, CrimeAdmin)
