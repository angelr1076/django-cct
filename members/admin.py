from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'profile_pic')
    list_display_links = ('id', 'user')
    search_fields = ('user',)
    list_filter = ('user',)
    list_per_page = 25

admin.site.register(Profile, ProfileAdmin)