from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class ShowCV(TemplateView):
    template_name = 'cv/index.html'
