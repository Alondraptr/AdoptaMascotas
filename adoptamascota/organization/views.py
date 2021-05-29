from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Organization
from django.urls import reverse, reverse_lazy
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
            # TODO: Rael hace lo que tenes que hacer
            return render(request,'organization/form.html',{'form': form, 'erros': form.errors})
    else:
        form = OrganizationAddForm()

    return render(request,'organization/form.html',{'form': form})


class OrganizationListView(ListView):
    model = Organization
    template_name = 'organization/index.html'

    def get_queryset(self):
        return self.model.objects.all()

class OrganizationDetailView(DetailView):
    model = Organization

class OrganizationUpdateView(SuccessMessageMixin, UpdateView):
    model = Organization
    form_class = OrganizationAddForm
    template_name = 'organization/form.html'

    def get_success_url(self):
        org_id = self.object.pk
        return reverse_lazy('show', kwargs={ 'pk': org_id })

class OrganizationDeleteView( DeleteView):
    model = Organization
    template_name = 'organization/show.html'
    success_url = reverse_lazy('index')