# from django import forms
# from django.utils.translation import ugettext as _
# from django import forms
# from.models import Education
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
#
# EDUCATIONLEVEL = (
#     ('Level 5', 'Leaving Cert.'),
#     ('Level 6', 'Post-Leaving Cert. Course'),
#     ('Level 7', 'Ordinary Bachelor Degree'),
#     ('Level 8', 'Honours Bachelor Degree'),
#     ('Level 9', 'Master\'s Degree'),
#     ('Level 10', 'Doctorate')
# )
#
# CAO_CODE = (
#     ('AL', 'Athlone Institute of Technology (AIT)'),
#     ('CW', 'Institute of Technology, Carlow (Carlow IT)'),
#     ('PC', 'Carlow College, St Patrick’s,'),
#     ('CR', 'Cork Institute of Technology (CIT)'),
#     ('CK', 'University College Cork (UCC)'),
#     ('GC', 'Griffith College Cork'),
#     ('AC', 'American College Dublin'),
#     ('CT', 'CCT College Dublin'),
#     ('CM', 'Marino Institute of Education'),
#     ('DS', 'Dorset College'),
#     ('DB', 'Dublin Business School'),
#     ('DC', 'Dublin City University (DCU)'),
#     ('DL', 'Dún Laoghaire Institute of Art'),
#     ('GC', 'Griffith College Dublin'),
#     ('ID', 'ICD Business School'),
#     ('AD', 'National College of Art and Design'),
#     ('NC', 'National College of Ireland (NCI)'),
#     ('RC', 'Royal College of Surgeons'),
#     ('NM', 'St Nicholas Montessori College'),
#     ('TU', 'Technological University Dublin (TU Dublin)'),
#     ('TR', 'Trinity College Dublin (TCD)'),
#     ('DN', 'University College Dublin (UCD)'),
#     ('DK', 'Dundalk Institute of Technology'),
#     ('GA', 'Galway-Mayo Institute of Technology'),
#     ('GY', 'National University of Ireland, Galway (NUIG)'),
#     ('GB', 'Galway Business School'),
#     ('MI', 'Mary Immaculate College'),
#     ('GC', 'Griffith College Limerick'),
#     ('CI', 'Irish College of Humanities and Applied Sciences'),
#     ('LC', 'Limerick Institute of Technology (LIT)'),
#     ('LM', 'University of Limerick (UL)'),
#     ('MU', 'Pontifical University, St Patrick’s College'),
#     ('MH', 'Maynooth University'),
#     ('GY', 'Shannon College of Hotel Management'),
#     ('AS', 'St Angela\'s College'),
#     ('SG', 'Institute of Technology, Sligo'),
#     ('TL', 'Institute of Technology, Tralee (ITT)'),
#     ('WD', 'Waterford Institute of Technology (WIT)')
# )
#
#
# class EducationForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#
#     class Meta:
#         model = Education
#         fields = ("EducationInstitutionName", "EducationLevel", "EducationStartDate", "EducationEndDate", "EducationCaoCode", "EducationDesc")
#
#     def save(self, commit=True):
#         edu = super(EducationForm, self).save(commit=False)
#         edu.EducationInstitutionName = self.cleaned_data['EducationInstitutionName']
#         edu.EducationLevel = self.cleaned_data['EducationLevel']
#         edu.EducationStartDate = self.cleaned_data['EducationStartDate']
#         edu.EducationEndDate = self.cleaned_data['EducationEndDate']
#         edu.EducationCaoCode = self.cleaned_data['EducationCaoCode']
#         edu.EducationDesc = self.cleaned_data['EducationDesc']
#         if commit:
#             edu.save()
#         return edu