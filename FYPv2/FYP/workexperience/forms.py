from django import forms
import FYP
from pages.models import WorkExperience


class WorkExperienceForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = WorkExperience
        fields = ('EmployerName', 'EmployerStartDate', 'EmployerEndDate', 'EmployerDesc')

    def save(self, commit=True):
        work = super(WorkExperienceForm, self).save(commit=False)
        work.WorkExperienceName = self.cleaned_data['EmployerName']
        work.WorkExperienceStartDate = self.cleaned_data['EmployerStartDate']
        work.WorkExperienceEndDate = self.cleaned_data['EmployerEndDate']
        work.WorkExperienceDesc = self.cleaned_data['EmployerDesc']
        work.save()
        return work