
        
from django import forms
from .models import InsuranceData

class InsuranceForm(forms.ModelForm):
    class Meta:
        model = InsuranceData
        fields = ['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges']
        
