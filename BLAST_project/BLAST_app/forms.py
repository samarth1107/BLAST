from django import forms

class HomeForm(forms.Form):
    sequence = forms.CharField(widget=forms.Textarea, label='Query Sequence')