from django import forms

class MyForm(forms.Form):
    name = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea, required=False)

