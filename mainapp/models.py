from django.db import models
from django.utils.translation import ugettext_lazy as _
import random
import string


# Url model
class Url(models.Model):
    target_url = models.TextField(null=False, blank=False)
    shortcode = models.CharField(max_length=10, null=True, blank=True)

    created_at = models.DateTimeField(
        _("Created at"),
        auto_now_add=True,
        help_text=_("When url was shortened")
    )

    def save(self, *args, **kwargs):
        self.shortcode = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
        super(Url, self).save(*args, **kwargs)

    def __str__(self):
        return self.target_url
