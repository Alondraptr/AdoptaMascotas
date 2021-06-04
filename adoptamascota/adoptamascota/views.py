from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import Template, Context
from django.template import loader
from organization.models import Organization
from pet.models import Pet
from django.contrib.auth.models import User


def index(request):
    context = {
    	'pets' : Pet.objects.all(),
        'organizations': Organization.objects.all()
    }
    return render(request, 'index.html', context)

def blog(request):
	template = loader.get_template("blog_index.html")
	context = {}
	return HttpResponse(template.render(context, request))



