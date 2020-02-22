from django import forms
import FYP
from pages.models import Cv, Education, CustomUser, Skills, WorkExperience


class CvForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Cv
        fields = ('user','CvName', 'CvEducation', 'CvSkills', 'CvWorkExperience')

        def __init__(self, *args, **kwargs):
            self._user = kwargs.pop('user')
            super(CvForm, self).__init__(*args, **kwargs)

        def save(self, commit=True):

            user_ids = CustomUser.objects.filter(username=self.request.user).values_list('id', flat=True)



            cv = super(CvForm, self).save(commit=False)
            cv.user = self.request.user.id
            cv.CvName = self.cleaned_data['CvName']
            if user_ids:
                for uid in user_ids:
                    cv.CvEducation = Education.objects.filter(user__id=uid)
                    cv.CvSkills = Skills.objects.filter(user__id=uid)
                    cv.CvWorkExperience = WorkExperience.objects.filter(user__id=uid)
            if commit:
                cv.save()
                self.save_m2m()
            return cv