
from .models import Link, Profile # Direct import without . prefix
from django.contrib import admin

class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'visit_count', 'click_count')

admin.site.register(Link)
admin.site.register(Profile)
