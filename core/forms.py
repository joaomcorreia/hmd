# core/forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Naam", max_length=120)
    email = forms.EmailField(label="E-mail")
    phone = forms.CharField(label="Telefoon", max_length=50, required=False)
    message = forms.CharField(label="Bericht", widget=forms.Textarea)

    # honeypot
    bedrijf_fax = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean_bedrijf_fax(self):
        if self.cleaned_data.get("bedrijf_fax"):
            raise forms.ValidationError("Spam detected.")
        return ""
