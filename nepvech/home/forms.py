
from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields=("__all__")

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields=("__all__")