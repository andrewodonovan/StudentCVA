from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Education


class EducationList(ListView):
    model = Education


class EducationView(DetailView):
    model = Education


class EducationCreate(CreateView):
    model = Education
    fields = ['EducationInstitutionName', 'EducationLevel', 'EducationStartDate', 'EducationEndDate', 'EducationCaoCode', 'EducationDesc']
    success_url = reverse_lazy('Education_list')


class EducationUpdate(UpdateView):
    model = Education
    fields = ['EducationInstitutionName', 'EducationLevel', 'EducationStartDate', 'EducationEndDate', 'EducationCaoCode', 'EducationDesc']
    success_url = reverse_lazy('Education_list')


class EducationDelete(DeleteView):
    model = Education
    success_url = reverse_lazy('Education_list')
