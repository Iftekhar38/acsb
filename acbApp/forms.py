from django import forms
from django.forms import Textarea


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'size':50}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'size':50}))
    phone = forms.IntegerField(widget=forms.TextInput(attrs={'size':50}))
    address = forms.CharField(widget=forms.TextInput(attrs={'size':50}))
    message = forms.CharField(widget=forms.Textarea(attrs={'name':'message', 'rows':10, 'cols':53}))