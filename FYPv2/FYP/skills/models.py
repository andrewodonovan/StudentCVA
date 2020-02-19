# from django.db import models
# from django.urls import reverse
# from django.utils.translation import ugettext as _
#
# class Skills(models.Model):
#     SkillsName = models.CharField(verbose_name=_('Skill Name'), max_length=100, default=None)
#     SkillsDesc = models.CharField(verbose_name=_('Skill Description'), max_length=250, default=None)
#
#     def __str__(self):
#         return self.SkillName
#
#     def get_absolute_url(self):
#         return reverse('Skills_edit', kwargs={'pk': self.pk})
