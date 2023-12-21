from django import forms
from .models import Progress

class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ['completed', 'date_completed']

class TexteForm(forms.Form):
    texte = forms.CharField(widget=forms.Textarea)
