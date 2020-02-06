from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext as _


class CustomUser(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    UserName = models.CharField(verbose_name=_('Full Name'), max_length=100, default=None)
    UserDOB = models.DateField(verbose_name=_('DOB'), default=None)
    UserPhone = models.CharField(verbose_name=_('Phone Number'), max_length=13, default=None)
    UserEmail = models.EmailField(verbose_name=_('Email'), default=None)
    UserAddress = models.CharField(verbose_name=_('Address'), max_length=250, default=None)

    def __str__(self):
        return f'{self.UserName} Profile'
