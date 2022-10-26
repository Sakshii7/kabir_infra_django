from django import forms
from .models import *


class ClientForm(forms.ModelForm):
    street = forms.CharField(
        widget=forms.Textarea(
            attrs={"placeholder": "Street..", }
        ),
    )

    class Meta:
        model = Clients
        fields = ["street"]
