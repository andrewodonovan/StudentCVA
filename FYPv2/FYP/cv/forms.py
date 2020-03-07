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


class CvUploadForm(forms.Form):
    cv_file = forms.FileField( label='Select a PDF CV')
    cv_name = forms.CharField(label='CV Name')

    def clean(self):
        cleaned_data = super(CvUploadForm, self).clean()

        text = cleaned_data.get('cv_name')


        return cleaned_data