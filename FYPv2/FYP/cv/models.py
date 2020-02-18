from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext as _

from FYP import education, users, skills, workexperience


class Cv(models.Model):
    CvName = models.CharField(verbose_name=_('CvName'), max_length=100, default=None)
    CvUser = models.ForeignKey(users, on_delete=models.CASCADE)
    CvEducation = models.ForeignKey(education, on_delete=models.CASCADE)
    CvSkills = models.ForeignKey(skills, on_delete=models.CASCADE)
    CvWorkExperience = models.ForeignKey(workexperience, on_delete=models.CASCADE)

    def __str__(self):
        return self.CvName
