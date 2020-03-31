from django import forms


class ShorteningForm(forms.Form):
    url = forms.CharField()
