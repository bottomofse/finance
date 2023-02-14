from django.shortcuts import render

from django.views import generic
from django.views.generic import TemplateView

class IndexTemplateView(TemplateView):
    template_name = 'finchart/index.html'
