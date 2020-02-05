from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext as _
from django.utils import timezone

# Create your models here.
class UserProfile(models.Model):
    UserName = models.CharField(verbose_name=_('Full Name'),max_length=100, default=None)
    UserDOB = models.DateField(verbose_name=_('Age'),default=None)
    UserPhone = models.CharField(verbose_name=_('Phone Number'),max_length=13, default=None)
    UserEmail = models.EmailField(verbose_name=_('Email'),default=None)
    UserAddress = models.CharField(verbose_name=_('Address'), max_length=250, default=None)