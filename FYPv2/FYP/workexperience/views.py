from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

import FYP
from pages.models import WorkExperience, CustomUser


class WorkExperienceList(ListView):
    model = WorkExperience
    
    def get_queryset(self):
        user_ids = CustomUser.objects.filter(username=self.request.user).values_list('id', flat=True)
        if user_ids:
            for uid in user_ids:
                return WorkExperience.objects.filter(user__id=uid)
        else:
            return WorkExperience.objects.all()


class WorkExperienceView(DetailView):
    model = WorkExperience


class WorkExperienceCreate(CreateView):
    model = WorkExperience
    fields = ['EmployerName', 'EmployerStartDate', 'EmployerEndDate', 'EmployerDesc']
    success_url = reverse_lazy('WorkExperience_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(WorkExperienceCreate, self).form_valid(form)


class WorkExperienceUpdate(UpdateView):
    model = WorkExperience
    fields = ['EmployerName', 'EmployerStartDate', 'EmployerEndDate', 'EmployerDesc']
    success_url = reverse_lazy('WorkExperience_list')


class WorkExperienceDelete(DeleteView):
    model = WorkExperience
    success_url = reverse_lazy('WorkExperience_list')
