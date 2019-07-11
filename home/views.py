from django.views.generic import TemplateView
from team_app.models import (TeamModel, ContactModel, ServiceModel)
# Create your views here.


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team_members'] = TeamModel.objects.all()
        context['contacts'] = ContactModel.objects.all()
        context['services'] = ServiceModel.objects.all()
        return context
