from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from sorl.thumbnail import ImageField


class User(AbstractUser):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    photo = ImageField(upload_to="team", blank=True, verbose_name=_("Photo"))
    birth_day = models.DateField(null=True, blank=True, verbose_name=_("Birth day"))

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def __str__(self):
        return "{0} {1} ({2})".format(self.first_name, self.last_name, self.username)
