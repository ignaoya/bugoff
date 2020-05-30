from django import forms
from .models import Bug, Worknote

class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('name', 'description')

class BugCompleteForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('complete',)

class WorknoteForm(forms.ModelForm):
    class Meta:
        model = Worknote
        fields = ('name', 'description')
