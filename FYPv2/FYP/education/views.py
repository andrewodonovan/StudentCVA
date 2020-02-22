from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from pages.models import Education, CustomUser

class EducationList(LoginRequiredMixin, ListView):
    model = Education

    def form_valid(self, form):
        id = self.request.user.id
        return super(EducationList, self).form_valid(form)

    def get_queryset(self):
        user_ids = CustomUser.objects.filter(username=self.request.user).values_list('id', flat=True)
        if user_ids:
            for uid in user_ids:
                return Education.objects.filter(user__id=uid)
        else:
            return Education.objects.all()

        # for uname in user_ids:
        #     print(uname)
        #     print(self.request.user)
        #     return Education.objects.filter(id=uname)




class EducationView(DetailView):
    model = Education



class EducationCreate(CreateView):
    model = Education
    fields = ['EducationInstitutionName', 'EducationLevel', 'EducationStartDate', 'EducationEndDate',
              'EducationCaoCode', 'EducationDesc']
    success_url = reverse_lazy('Education_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EducationCreate, self).form_valid(form)


class EducationUpdate(UpdateView):
    model = Education

    fields = ['EducationInstitutionName', 'EducationLevel', 'EducationStartDate', 'EducationEndDate',
              'EducationCaoCode', 'EducationDesc']
    success_url = reverse_lazy('Education_list')


class EducationDelete(DeleteView):
    model = Education
    success_url = reverse_lazy('Education_list')
