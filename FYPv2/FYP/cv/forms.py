from django import forms
from django.views.generic.edit import FormMixin

import FYP
from pages.models import Cv, Education, CustomUser, Skills, WorkExperience


class CvForm(forms.ModelForm):
    class Meta:
        model = Cv
        fields = ('CvName', 'CvEducation', 'CvSkills', 'CvWorkExperience')

    def __init__(self, *args, **kwargs):
        # DO NOT REMOVE UNDER PENALTY OF DEATH!!!!!!!
        initial_arguments = kwargs.get('initial', None)
        initial_arguments_list = list(initial_arguments.values())
        user_id = initial_arguments_list[0]
        super(CvForm, self).__init__(*args, **kwargs)
        self.fields['CvEducation'].queryset = Education.objects.filter(user__id=user_id)
        self.fields['CvSkills'].queryset = Skills.objects.filter(user__id=user_id)
        self.fields['CvWorkExperience'].queryset = WorkExperience.objects.filter(user__id=user_id)
        # form.instance.user = self.request.user




    # def save(self, commit=False):
    #     cv = super(CvForm, self).save(commit=False)
    #     cv.user = self.request.user
    #     cv.CvName = self.cleaned_data['CvName']
    #     cv.CvEducation = self.cleaned_data['CvEducation']
    #     cv.CvSkills = self.cleaned_data['CvSkills']
    #     cv.CvWorkExperience = self.cleaned_data['CvWorkExperience']
    #     if commit:
    #         cv.save()
    #     return cv



