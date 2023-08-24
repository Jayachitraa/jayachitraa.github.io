from django import forms
from .models import ContEmpMast

class ContEmpMastForm(forms.ModelForm):
    class Meta:
        model = ContEmpMast
        fields = '__all__'  # You can replace this with a list of specific fields you want
