from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Url
from .utils import is_url


class ShorteningForm(forms.ModelForm):
    class Meta:
        model = Url
        exclude = ('shortcode', 'full_url')
        widgets = {
            'target_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Paste your URL here...')}),
        }

    def clean_target_url(self):
        url_inserted = self.cleaned_data['target_url']
        if not is_url(url_inserted): raise forms.ValidationError("You have to provide proper URL adress")

        return url_inserted
