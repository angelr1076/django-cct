from django.contrib import admin
from .models import Suspect


class SuspectAdmin(admin.ModelAdmin):
    list_display = ('id', 'in_custody', 'first_name', 'last_name', 'mugshot')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('last_name',)
    list_filter = ('last_name',)
    list_editable = ('in_custody',)
    list_per_page = 25

admin.site.register(Suspect, SuspectAdmin)
