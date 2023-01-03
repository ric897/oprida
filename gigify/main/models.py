from django.db import models
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import socket
socket.gethostbyname("")
from django.template.loader import render_to_string
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models.signals import post_save
from django.template.defaultfilters import slugify

# Create your models here.

class Case(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    textfield = models.TextField()
    slug = models.SlugField(max_length=250, primary_key=True, default=None)
    date = models.DateField(default = timezone.now)
    author = models.CharField(max_length=500, null=True)
    category = models.CharField(max_length=100)
    image = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        super().save(*args, **kwargs)

