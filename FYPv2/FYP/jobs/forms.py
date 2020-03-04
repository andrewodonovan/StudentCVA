from django import forms

#===============================================================
# https://docs.djangoproject.com/en/3.0/topics/forms/
#===============================================================

class JobForm(forms.Form):
    job_role = forms.CharField(label='Job Role:', max_length=200)
    job_location = forms.CharField(label='Job Location:', max_length=200)