from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm, CustomUserChangeForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


# ==================================================================================================================
# https://www.youtube.com/watch?v=CQ90L5jfldw&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=9&pbjreload=10
# ==================================================================================================================
@login_required
def ProfileView(request):
    if request.method == 'POST':
        u_form = CustomUserCreationForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()

            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = CustomUserChangeForm(instance=request.user)
        messages.success(request, f'Your account has been updated!')
    context = {
        'u_form': u_form,
    }
    return render(request, 'profile.html', context)
