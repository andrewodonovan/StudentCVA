from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext as _

import FYP
from FYP import settings


EDUCATIONLEVEL = (
    ('Level 5', 'Leaving Cert.'),
    ('Level 6', 'Post-Leaving Cert. Course'),
    ('Level 7', 'Ordinary Bachelor Degree'),
    ('Level 8', 'Honours Bachelor Degree'),
    ('Level 9', 'Master\'s Degree'),
    ('Level 10', 'Doctorate')
)

CAO_CODE = (
    ('N/A','N/A'),
    ('AL', 'Athlone Institute of Technology (AIT)'),
    ('CW', 'Institute of Technology, Carlow (Carlow IT)'),
    ('PC', 'Carlow College, St Patrick’s,'),
    ('CR', 'Cork Institute of Technology (CIT)'),
    ('CK', 'University College Cork (UCC)'),
    ('GC', 'Griffith College Cork'),
    ('AC', 'American College Dublin'),
    ('CT', 'CCT College Dublin'),
    ('CM', 'Marino Institute of Education'),
    ('DS', 'Dorset College'),
    ('DB', 'Dublin Business School'),
    ('DC', 'Dublin City University (DCU)'),
    ('DL', 'Dún Laoghaire Institute of Art'),
    ('GC', 'Griffith College Dublin'),
    ('ID', 'ICD Business School'),
    ('AD', 'National College of Art and Design'),
    ('NC', 'National College of Ireland (NCI)'),
    ('RC', 'Royal College of Surgeons'),
    ('NM', 'St Nicholas Montessori College'),
    ('TU', 'Technological University Dublin (TU Dublin)'),
    ('TR', 'Trinity College Dublin (TCD)'),
    ('DN', 'University College Dublin (UCD)'),
    ('DK', 'Dundalk Institute of Technology'),
    ('GA', 'Galway-Mayo Institute of Technology'),
    ('GY', 'National University of Ireland, Galway (NUIG)'),
    ('GB', 'Galway Business School'),
    ('MI', 'Mary Immaculate College'),
    ('GC', 'Griffith College Limerick'),
    ('CI', 'Irish College of Humanities and Applied Sciences'),
    ('LC', 'Limerick Institute of Technology (LIT)'),
    ('LM', 'University of Limerick (UL)'),
    ('MU', 'Pontifical University, St Patrick’s College'),
    ('MH', 'Maynooth University'),
    ('GY', 'Shannon College of Hotel Management'),
    ('AS', 'St Angela\'s College'),
    ('SG', 'Institute of Technology, Sligo'),
    ('TL', 'Institute of Technology, Tralee (ITT)'),
    ('WD', 'Waterford Institute of Technology (WIT)')
)

class CustomUser(AbstractUser):
    pass




class Education(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    EducationInstitutionName = models.CharField(verbose_name=_('Institution Name'), max_length=100, default=None)
    EducationLevel = models.CharField(verbose_name=_('Education Level'), choices=EDUCATIONLEVEL, max_length=100, default=None)
    EducationStartDate = models.DateField(verbose_name=_('Education Start Date'), default=None)
    EducationEndDate = models.DateField(verbose_name=_('Education End Date'), default=None)
    EducationCaoCode = models.CharField(choices=CAO_CODE, max_length=100, default=None)
    EducationDesc = models.CharField(verbose_name=_('Education Description'), max_length=250, default=None)


    def __str__(self):
        return self.EducationInstitutionName

    def get_absolute_url(self):
        return reverse('Education_edit', kwargs={'pk': self.pk})


class Skills(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    SkillsName = models.CharField(verbose_name=_('Skill Name'), max_length=100, default=None)
    SkillsDesc = models.CharField(verbose_name=_('Skill Description'), max_length=250, default=None)

    def __str__(self):
        return self.SkillsName

    def get_absolute_url(self):
        return reverse('Skills_edit', kwargs={'pk': self.pk})


class WorkExperience(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    EmployerName = models.CharField(verbose_name=_('Employer'), max_length=100, default=None)
    EmployerStartDate = models.DateField(verbose_name=_('Employer Start Date'), default=None)
    EmployerEndDate = models.DateField(verbose_name=_('Employer End Date'), default=None)
    EmployerDesc = models.CharField(verbose_name=_('Employer Description'), max_length=250, default=None)

    def __str__(self):
        return self.EmployerName



class Cv(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    CvName = models.CharField(verbose_name=_('CvName'), max_length=100, default=None)
    CvEducation = models.ForeignKey(Education, on_delete=models.CASCADE)
    CvSkills = models.ForeignKey(Skills, on_delete=models.CASCADE)
    CvWorkExperience = models.ForeignKey(WorkExperience, on_delete=models.CASCADE)

    def __str__(self):
        return self.CvName


