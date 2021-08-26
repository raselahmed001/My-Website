from django.forms import ModelForm
from django.forms.models import fields_for_model
from .models import Candidate

class JobApllyForm(ModelForm):
    class meta:
        model = Candidate
        fields = "__all__"