from django import forms
import FYP
from pages.models import Skills


class SkillsForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Skills
        fields = ("Skill Name", "Skill Description")

    def save(self, commit=True):
        skill = super(SkillsForm, self).save(commit=False)

        skill.SkillsName = self.cleaned_data['SkillsName']
        skill.SkillsDesc = self.cleaned_data['SkillsDesc']
        skill.save()
        return skill