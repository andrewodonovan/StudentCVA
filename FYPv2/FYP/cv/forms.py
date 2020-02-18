from django import forms
from .models import Cv


class CvForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Cv
        fields = ('CvName', 'CvUser', 'CvEducation', 'CvSkills', 'CvWorkExperience')

    def save(self, commit=True):
        cv = super(CvForm, self).save(commit=False)
        cv.CvName = self.cleaned_data['CvName']
        cv.CvUser = self.cleaned_data['CvUser']
        cv.CvEducation = self.cleaned_data['CvEducation']
        cv.CvSkills = self.cleaned_data['CvSkills']
        cv.CvWorkExperience = self.cleaned_data['CvWorkExperience']

        cv.save()
        return cv