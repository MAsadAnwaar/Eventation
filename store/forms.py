#from typing_extensions import Required





from django import forms
from .models.contact import contact


class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = "__all__"



