from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

import FYP
from pages.models import Skills, CustomUser


class SkillsList(ListView):
    model = Skills

    def get_queryset(self):
        user_ids = CustomUser.objects.filter(username=self.request.user).values_list('id', flat=True)
        if user_ids:
            for uid in user_ids:
                return Skills.objects.filter(user__id=uid)
        else:
            return Skills.objects.all()


class SkillsView(DetailView):
    model = Skills


class SkillsCreate(CreateView):
    model = Skills
    fields = ['SkillsName', 'SkillsDesc']
    success_url = reverse_lazy('Skills_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SkillsCreate, self).form_valid(form)


class SkillsUpdate(UpdateView):
    model = Skills
    fields = ['SkillsName', 'SkillsDesc']
    success_url = reverse_lazy('Skills_list')


class SkillsDelete(DeleteView):
    model = Skills
    success_url = reverse_lazy('Skills_list')
