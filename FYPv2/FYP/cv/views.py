from django.views.generic import TemplateView


class CvView(TemplateView):
    template_name = 'cv.html'
