from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template

# primera vista
def index(request):

	a = get_template("index.html")
	doc = a.render()
	return HttpResponse(doc)

def adopta(request):

	a = get_template("adopta_index.html")
	doc = a.render()
	return HttpResponse(doc)

def organizaciones(request):

	a = get_template("organizaciones_index.html")
	doc = a.render()
	return HttpResponse(doc)

def blog(request):

	a = get_template("blog_index.html")
	doc = a.render()
	return HttpResponse(doc)

def registro(request):

	a = get_template("register.html")
	doc = a.render()
	return HttpResponse(doc)


def ingreso(request):

	a = get_template("login.html")
	doc = a.render()
	return HttpResponse(doc)

