from django import forms
from .models import ExtraCurricular

class ExtraCurricularForm(forms.ModelForm):
    class Meta:
        model = ExtraCurricular
        fields = ['activity_name']