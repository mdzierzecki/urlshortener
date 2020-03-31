from django.db import models
from django.utils.translation import ugettext_lazy as _


# Url model
class Url(models.Model):
    target_url = models.TextField(null=False, blank=False)
    shortened_url = models.CharField(max_length=10, null=True, blank=True)

    created_at = models.DateTimeField(
        _("Created at"),
        auto_now_add=True,
        help_text=_("When url was shortened")
    )

    def __str__(self):
        return self.target_url
