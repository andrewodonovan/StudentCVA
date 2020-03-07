from datetime import datetime

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.http import FileResponse, Http404
from django.core.files.storage import FileSystemStorage

from django.views.decorators.clickjacking import xframe_options_exempt
from reportlab.pdfgen import canvas
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#================================================
#               BACKEND IMPORTS
#================================================
import re
import requests
from bs4 import BeautifulSoup as bs
import slate3k as slate
#================================================

import FYP
from pages.models import Cv, CustomUser, Education, Skills, WorkExperience
from .forms import CvForm, CvUploadForm


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

#==================================================================================================
# https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html
#==================================================================================================


def simple_upload(request):
    form = CvUploadForm(request.POST, request.FILES)
    if form.is_valid():
        if request.method == 'POST' and request.FILES['cv_file']:
                cv_file = request.FILES['cv_file']
                fs = FileSystemStorage()
                filename = fs.save(cv_file.name, cv_file)
                return pdf_view(request)



    return render(request, 'pages/cvupload.html', {'form':form})


def pdf_view(request):
    cv_file = request.FILES['cv_file']

    if cv_file:
        fs = FileSystemStorage()
        file_name = cv_file.name
        context = {'cv_path': file_name}





    except FileNotFoundError:
        raise Http404()

    return render(request, 'pages/cv-display.html', context)



# Set the naming convention for the different sections
file_name_format = 'section_#.txt'

# Splitting function
def text_splitter(fn):
    # Apply the naming convention for the filename using the number passed into the function
    filename = file_name_format.replace('#', str(fn))
    # Write to the file and save the file to a variable
    out = open(filename, 'w')
    # Return the variable
    return out


# def create_pdf(request):
#     # Create the HttpResponse object with the appropriate PDF headers.
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
#
#     # Create the PDF object, using the response object as its "file."
#     p = canvas.Canvas(response)
#
#     # Draw things on the PDF. Here's where the PDF generation happens.
#     # See the ReportLab documentation for the full list of functionality.
#     p.drawString(100, 100, "Hello world.")
#
#     # Close the PDF object cleanly, and we're done.
#     p.showPage()
#     p.save()
#     return response
