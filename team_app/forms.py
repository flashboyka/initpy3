from django import forms
from ckeditor.widgets import CKEditorWidget

from team_app.models import TeamModel


class TeamForm(forms.ModelForm):
    skills = forms.CharField(widget=CKEditorWidget)

    class Meta:
        model = TeamModel
        fields = '__all__'
