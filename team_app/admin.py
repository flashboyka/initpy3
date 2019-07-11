from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from team_app.models import (TeamModel, ContactModel)
# Register your models here.


@admin.register(TeamModel)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['user', 'position']
    autocomplete_fields = ('user',)
    fieldsets = (
        (None, {
            'fields': (('user', 'position'),)
        }),
        (_('Skills'), {
            'fields': ('skills',)
        }),
    )

@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['phone', 'fax', 'address', 'email']
    fieldsets = (
        (_('Contacts'), {
            'fields': (('phone', 'email'), 'fax')
        }),
        (_('Address'), {
            'fields': ('address',)
        })
    )
