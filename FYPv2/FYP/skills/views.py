from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Skills


class SkillsList(ListView):
    model = Skills


class SkillsView(DetailView):
    model = Skills


class SkillsCreate(CreateView):
    model = Skills
    fields = ['SkillsName', 'SkillsDesc']
    success_url = reverse_lazy('Skills_list')


class SkillsUpdate(UpdateView):
    model = Skills
    fields = ['SkillsName', 'SkillsDesc']
    success_url = reverse_lazy('Skills_list')


class SkillsDelete(DeleteView):
    model = Skills
    success_url = reverse_lazy('Skills_list')
