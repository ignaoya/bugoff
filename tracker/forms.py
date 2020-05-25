from django import forms
from .models import Bug, Worknote

class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('description',)

class WorknoteForm(forms.ModelForm):
    class Meta:
        model = Worknote
        fields = ('name', 'description')
