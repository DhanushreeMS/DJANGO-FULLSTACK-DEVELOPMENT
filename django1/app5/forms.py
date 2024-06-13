from django import forms
from .models import StudentRegistration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        fields = ['name', 'college', 'course']
