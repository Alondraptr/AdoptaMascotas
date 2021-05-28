from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Organization
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseForbidden, HttpResponseRedirect

class OrganizationListView(ListView):
    model = Organization

class OrganizationDetailView(DetailView):
    model = Organization

class OrganizationCreateView(SuccessMessageMixin, CreateView):
    model = Organization
    success_message = 'Organizacion Creado Correctamente !'
    fields = ['name', 'description']

    # Redireccionamos a la página principal luego de crear un registro o Organization
    def get_success_url(self):
        return reverse('index')

class OrganizationActualizar(SuccessMessageMixin, UpdateView):
    model = Organization
    form = Organization
    fields = "__all__"
    success_message = 'Organizacion Actualizado Correctamente !'

    # Redireccionamos a la página principal luego de actualizar un registro o Organization
    def get_success_url(self):
        return reverse('index')

class OrganizationEliminar(SuccessMessageMixin, DeleteView):
    model = Organization
    form = Organization
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o Organization
    def get_success_url(self):
        success_message = 'Organizacion Eliminado Correctamente !'
        messages.success(self.request, (success_message))
        return reverse('index')