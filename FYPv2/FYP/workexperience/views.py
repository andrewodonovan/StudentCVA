from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import WorkExperience


class WorkExperienceList(ListView):
    model = WorkExperience


class WorkExperienceView(DetailView):
    model = WorkExperience


class WorkExperienceCreate(CreateView):
    model = WorkExperience
    fields = ['EmployerName', 'EmployerStartDate', 'EmployerEndDate', 'EmployerDesc']
    success_url = reverse_lazy('WorkExperience_list')


class WorkExperienceUpdate(UpdateView):
    model = WorkExperience
    fields = ['EmployerName', 'EmployerStartDate', 'EmployerEndDate', 'EmployerDesc']
    success_url = reverse_lazy('WorkExperience_list')


class WorkExperienceDelete(DeleteView):
    model = WorkExperience
    success_url = reverse_lazy('WorkExperience_list')
