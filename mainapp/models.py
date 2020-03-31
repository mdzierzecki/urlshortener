from django.db import models
from django.utils.translation import ugettext_lazy as _
from .utils import shortcode_generator


# URL model
class Url(models.Model):
    target_url = models.TextField(null=False, blank=False)
    shortcode = models.CharField(max_length=10, null=True, blank=True)
    full_url = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(
        _("Created at"),
        auto_now_add=True,
        help_text=_("When url was shortened")
    )

    @staticmethod
    def assign_shortcode(url, http):
        url.shortcode = shortcode_generator()
        url.full_url = "{}/{}".format(http, url.shortcode)
        url.save()

    def __str__(self):
        return "{} - {}".format(self.full_url, self.target_url)
