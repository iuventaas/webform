from django import forms

class AddForm(forms.Form):
    item = forms.CharField(label='Item', max_length=100)
    value = forms.CharField(label='Value', max_length=100)
