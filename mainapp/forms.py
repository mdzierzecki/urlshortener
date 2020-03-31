from django import forms
from .models import Url


class ShorteningForm(forms.ModelForm):
    class Meta:
        model = Url
        exclude = ('shortcode', 'full_url')

