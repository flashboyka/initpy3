from team_app.models import (
    TeamModel,
    ContactModel,
    ServiceModel,
    AboutModel,
    CertificatesModel,
)


class TeamMiddleware:
    def __init__(self, response):
        self.response = response

    def __call__(self, request):
        return self.response(request)

    def process_template_response(self, request, response):
        response.context_data['team_members'] = TeamModel.objects.all()
        response.context_data['contacts'] = ContactModel.objects.all()
        response.context_data['services'] = ServiceModel.objects.all()
        response.context_data['abouts'] = AboutModel.objects.all()
        response.context_data['certs'] = CertificatesModel.objects.all()
        return response
