from django import forms

class ItemForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea())