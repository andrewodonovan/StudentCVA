from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

import FYP
from pages.models import Cv, CustomUser, Education, Skills, WorkExperience
from .forms import CvForm


class CvList(ListView):
    model = Cv
    fields = ['CvName', 'CvEducation', 'CvSkills', 'CvWorkExperience']
    success_url = reverse_lazy('Cv_list')

    def get_queryset(self):
        user_ids = CustomUser.objects.filter(username=self.request.user).values_list('id', flat=True)
        if user_ids:
            for uid in user_ids:
                return Cv.objects.filter(user__id=uid)
        else:
            return Cv.objects.all()


class CvView(DetailView):
    model = Cv

class CvCreate(CreateView):
    model = Cv
    success_url = reverse_lazy('Cv_list')
    form_class = CvForm
    exclude = ['user']

    def get_initial(self):
        self.initial.update({ 'created_by': self.request.user.id })
        return self.initial

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CvCreate, self).form_valid(form)

    def get_queryset(self):
        user_ids = CustomUser.objects.filter(username=self.request.user).values_list('id', flat=True)
        if user_ids:
            for uid in user_ids:
                return Cv.objects.filter(user__id=uid)
        else:
            return Cv.objects.all()


class CvUpdate(UpdateView):
    model = Cv
    form_class = CvForm
    success_url = reverse_lazy('Cv_list')


class CvDelete(DeleteView):
    model = Cv
    success_url = reverse_lazy('Cv_list')
