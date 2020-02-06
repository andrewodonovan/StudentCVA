from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm, CustomUserChangeForm, ProfileUpdateForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


@login_required
def ProfileView(request):
        u_form = CustomUserChangeForm()
        p_form = ProfileUpdateForm()
        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, 'profile.html', context)
