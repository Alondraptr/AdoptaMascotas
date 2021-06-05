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
from .filters import PetTypeFilter
from organization.models import Organization
from users.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404


class PetListView(ListView):
    model = Pet
    template_name = 'pet/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter']= PetTypeFilter(self.request.GET, queryset=self.get_queryset())
        return context

class OrgListView(ListView):
    model = Pet
    template_name = 'pet/org_pets.html'

    def get_queryset(self):
        organization = Organization.objects.get(user=self.request.user)
        return Pet.objects.filter(organization=organization)

class PetDetailView(DetailView):
    model = Pet

class PetCreateView(LoginRequiredMixin, CreateView):
    model = Pet
    form_class = PetForm
    template_name = 'pet/form.html'

    def get_success_url(self):
        pet_id = self.object.pk
        return reverse_lazy('pet_show', kwargs={ 'pk': pet_id })

    def get_context_data( self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the pets
        pet_type_list = ['Perro', 'Gato', 'Conejo', 'Aves']
        organization = Organization.objects.get(user=self.request.user)
        context['pet_type'] = pet_type_list
        context['organization'] = organization.id
        return context

class PetUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Pet
    form_class = PetForm
    template_name = 'pet/form.html'

    def get_queryset(self):
        user = self.request.user
        organization = Organization.objects.get(user=user)
        return Pet.objects.filter(organization=organization.id)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        pet_type_list = ['Perro', 'Gato', 'Conejo', 'Aves']
        organization = Organization.objects.get(user=self.request.user)
        context['pet_type'] = pet_type_list
        context['organization'] = organization.id
        return context

    def get_success_url(self):
        pet_id = self.object.pk
        return reverse_lazy('pet_show', kwargs={ 'pk': pet_id })

class PetDeleteView( LoginRequiredMixin, DeleteView):
    model = Pet
    template_name = 'pet/show.html'
    success_url = reverse_lazy('pet_index')

    def get_queryset(self):
        user = self.request.user
        organization = Organization.objects.get(user=user)
        return Pet.objects.filter(organization=organization.id)