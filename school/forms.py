from django import forms
from .models import ExtraCurricular, Guardian

class ExtraCurricularForm(forms.ModelForm):
    class Meta:
        model = ExtraCurricular
        fields = ['activity_name']


class GuardianForm(forms.ModelForm):
    class Meta:
        model = Guardian
        fields = ['first_name', 'last_name', 'relation', 'phone_number', 'address']