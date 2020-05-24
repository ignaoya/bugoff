from django import forms
from .models import Worknote

class WorknoteForm(forms.ModelForm):
    class Meta:
        model = Worknote
        fields = ('name', 'description')
