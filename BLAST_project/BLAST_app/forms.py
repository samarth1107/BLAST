from django import forms

class HomeForm(forms.Form):
    sequence = forms.CharField(widget=forms.Textarea(attrs={'required': True, 'class' : 'form-control'}), label="Query Sequence :    ", min_length=15)
    data_base_path = forms.CharField(widget=forms.TextInput(attrs={'required': True}), label="Database path:  ")