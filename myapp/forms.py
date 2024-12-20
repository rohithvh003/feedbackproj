from typing import Any
from django import forms
class Feedbackform(forms.Form):
    name = forms.CharField()
    id = forms.IntegerField()
    email = forms.EmailField()
    dept  = forms.CharField()
    batch = forms.IntegerField()
    feedback = forms.CharField(widget= forms.Textarea) 
    def clean_name(self):
        n=self.cleaned_data['name']
        if len(n)<5:
            raise forms.ValidationError('Min no of char greater than 5')
        return n
    def clean_id(self):
        n=self.cleaned_data['id']
        if n<=0:
            raise forms.ValidationError('id mus be positive')
        return n