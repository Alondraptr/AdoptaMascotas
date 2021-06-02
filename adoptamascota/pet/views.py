from django.db.models.fields import PositiveIntegerRelDbTypeMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pet
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseForbidden, HttpResponseRedirect
from .form import PetForm
from organization.models import Organization

class PetListView(ListView):
    model = Pet
    template_name = 'pet/index.html'

    def get_queryset(self):
        return self.model.objects.all()

class PetDetailView(DetailView):
    model = Pet

class PetCreateView(CreateView):
    model = Pet
    form_class = PetForm
    template_name = 'pet/form.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['pet_type'] = ['Perro', 'Gato', 'Conejo', 'Aves']
        return context

    def get_success_url(self):
        pet_id = self.object.pk
        return reverse_lazy('pet_show', kwargs={ 'pk': pet_id })

class PetUpdateView(SuccessMessageMixin, UpdateView):
    model = Pet
    form_class = PetForm
    template_name = 'pet/form.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['pet_type'] = ['Perro', 'Gato', 'Conejo', 'Aves']
        return context

    def get_success_url(self):
        pet_id = self.object.pk
        return reverse_lazy('pet_show', kwargs={ 'pk': pet_id })

class PetDeleteView( DeleteView):
    model = Pet
    template_name = 'pet/show.html'
    success_url = reverse_lazy('pet_index')