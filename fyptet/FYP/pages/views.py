from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'index.html'


class CvView(TemplateView):
    template_name = 'createcv.html'


class profileView(TemplateView):
    template_name = 'profile.html'
