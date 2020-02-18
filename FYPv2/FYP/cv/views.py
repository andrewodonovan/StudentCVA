from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Cv


class CvList(ListView):
    model = Cv


class CvView(DetailView):
    model = Cv


class CvCreate(CreateView):
    model = Cv
    fields = ['CvName', 'CvUser', 'CvEducation', 'CvSkills', 'CvWorkExperience']
    success_url = reverse_lazy('Cv_list')


class CvUpdate(UpdateView):
    model = Cv
    fields = ['CvName', 'CvUser', 'CvEducation', 'CvSkills', 'CvWorkExperience']
    success_url = reverse_lazy('Cv_list')


class CvDelete(DeleteView):
    model = Cv
    success_url = reverse_lazy('Cv_list')
