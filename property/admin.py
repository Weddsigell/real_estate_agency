from django.contrib import admin
from .models import Flat, Complaint, Owner


class ItemInline(admin.StackedInline):
    model = Owner.flats.through
    raw_id_fields = ['owner']
    list_display = ['owner']

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ['new_building']
    list_filter = ['new_building', 'price', 'rooms_number', 'floor', 'has_balcony', 'active']
    raw_id_fields = ['likes']
    inlines = [ItemInline]
    exclude = ["flats"]

class ReportAdmin(admin.ModelAdmin):
    raw_id_fields = ['flat']
    list_display = ('flat', 'report')

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('owner', 'owners_phonenumber',)
    raw_id_fields = ['flats']

admin.site.register(Flat, AuthorAdmin)
admin.site.register(Complaint, ReportAdmin)
admin.site.register(Owner, OwnerAdmin)
