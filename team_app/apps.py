from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TeamAppConfig(AppConfig):
    name = 'team_app'
    verbose_name = _("Team")
