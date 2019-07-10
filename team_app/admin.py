from django.contrib import admin
from team_app.models import TeamModel
from team_app.forms import TeamForm
# Register your models here.


@admin.register(TeamModel)
class TeamAdmin(admin.ModelAdmin):
    form = TeamForm
    list_display = ['user', ]
    autocomplete_fields = ('user',)
