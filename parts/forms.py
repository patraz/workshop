from django import forms
from .models import Part

class AddPartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ['nazwa', 'opis', 'ilość', 'kupione_od', 'dodane']
        