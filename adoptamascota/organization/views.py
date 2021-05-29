from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Organization
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseForbidden, HttpResponseRedirect
from .form import OrganizationAddForm

def create(request):
    if request.method == 'POST':
        form = OrganizationAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            import pdb; pdb.set_trace()
            # TODO: Rael hace lo que tenes que hacer
            return render(request,'organization/create.html',{'form': form, 'erros': form.errors})
    else:
        form = OrganizationAddForm()

    return render(request,'organization/create.html',{'form': form})


class OrganizationListView(ListView):
    model = Organization

class OrganizationDetailView(DetailView):
    model = Organization

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