from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, FormView

from cv.forms import ContactForm


# Create your views here.
class ShowCV(TemplateView):
    template_name = 'cv/index.html'


class FormCV(FormView):
    form_class = ContactForm
    template_name = 'static/cv/contact-form-t.html'

    def form_valid(self, form):
        form.senf_mail()
        return super().form_valid(form)



