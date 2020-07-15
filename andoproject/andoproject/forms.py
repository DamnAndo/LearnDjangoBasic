from django import forms
from django.core import validators

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    subject = forms.CharField(widget=forms.Textarea)
    honeypot = forms.CharField(widget=forms.HiddenInput,required=False,
                               validators=[validators.MaxLengthValidator(0)])

    # Cara 1 Validasi
    # def clean_honeypot(self):
    #     honeypot = self.cleaned_data['honeypot']
    #     if len(honeypot):
    #         raise forms.ValidationError('Engga bOleh diisi dong')
    #     return honeypot