from django import forms
from .models import registerform

class myregisterForm(forms.ModelForm):
    class Meta:
        model=registerform
        fields=['Name','Age','Address','Contact','Email']