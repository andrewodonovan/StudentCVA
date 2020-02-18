from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext as _

class WorkExperience(models.Model):
    Employer = models.CharField(verbose_name=_('Employer'), max_length=100, default=None)
    EmployerStartDate = models.DateField(verbose_name=_('Employer Start Date'), default=None)
    EmployerEndDate = models.DateField(verbose_name=_('Employer End Date'), default=None)
    EmployerDesc = models.CharField(verbose_name=_('Employer Description'), max_length=250, default=None)


    def __str__(self):
        return self.EmployerName

