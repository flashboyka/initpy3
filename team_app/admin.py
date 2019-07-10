from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from team_app.models import TeamModel
from team_app.forms import TeamForm
# Register your models here.


@admin.register(TeamModel)
class TeamAdmin(admin.ModelAdmin):
    #form = TeamForm
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
