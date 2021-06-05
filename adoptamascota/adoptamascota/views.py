from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.template import Template, Context
from django.template import loader
from organization.models import Organization
from pet.models import Pet
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from .form import ContactAdminForm



def index(request):
    context = {
    	'pets' : Pet.objects.all(),
        'organizations': Organization.objects.all()
    }
    return render(request, 'index.html', context)

def contactAdmin(request):
    template = loader.get_template("contact_admin.html")
    context = {}
    if request.method == 'GET':
        form = ContactAdminForm()
    else:
        form = ContactAdminForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/')
    return render(request, "contact_admin.html", {'form': form})


