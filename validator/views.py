# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import CreateView,DetailView
from .forms import PersonModelForm,VerifyID

from django.views.generic.edit import FormView
from .models import Person

# Create your views here.

class PersonCreateView (CreateView):
    form_class = PersonModelForm
    template_name = 'form.html'


    def form_valid(self, form):
        instance = form.save(commit=False)
        return super(PersonCreateView, self).form_valid(form)

class PersonDetailView(DetailView):

    def get_queryset(self):
        return Person.objects.all()

class IdValidateView (FormView):
    form_class = VerifyID
    template_name = 'validate_id.html'
    success_url = '/ids/validate/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        #form.clean_id()

        return super(IdValidateView, self).form_valid(form)