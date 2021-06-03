from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import Template, Context

from django.template import loader
from django.contrib.auth.models import User


# primera vista
def index(request):
	template = loader.get_template("index.html")
	context = {}
	return HttpResponse(template.render(context, request))

def adopta(request):
	template = loader.get_template("adopta_index.html")
	context = {}
	return HttpResponse(template.render(context, request))

def blog(request):
	template = loader.get_template("blog_index.html")
	context = {}
	return HttpResponse(template.render(context, request))



