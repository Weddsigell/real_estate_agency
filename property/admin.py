from django.contrib import admin
from .models import Flat, Complaint


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ['new_building']
    list_filter = ['new_building', 'price', 'rooms_number', 'floor', 'has_balcony', 'active']
    raw_id_fields = ['likes']

class ReportAdmin(admin.ModelAdmin):
    raw_id_fields = ['flat']

admin.site.register(Flat, AuthorAdmin)
admin.site.register(Complaint, ReportAdmin)
