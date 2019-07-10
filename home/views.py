from django.views.generic import TemplateView
from team_app.models import TeamModel
# Create your views here.


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team_members'] = TeamModel.objects.all()
        return context
