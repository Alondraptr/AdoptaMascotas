from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Blog
from django.contrib.auth.models import User
import operator
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .form import BlogForm
from django.contrib.auth.mixins import LoginRequiredMixin
from organization.models import Organization

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/index.html'

    def get_queryset(self):
        return self.model.objects.all()


class BlogDetailView(DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        images_url = []
        if self.object.img_1:
            images_url.append(self.object.img_1.url)
        if self.object.img_2:
            images_url.append(self.object.img_2.url)
        if self.object.img_3:
            images_url.append(self.object.img_3.url)
        if self.object.img_4:
            images_url.append(self.object.img_4.url)
        context['images_url'] = images_url
        return context

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/form.html'

    def get_context_data( self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        org_id = Organization.objects.get(user=self.request.user).id
        context['org_id'] = org_id
        return context

    def get_success_url(self):
        blog_id = self.object.pk
        return reverse_lazy('blog_show', kwargs={ 'pk': blog_id })


class BlogUpdateView(LoginRequiredMixin,SuccessMessageMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/form.html'

    def get_context_data( self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        org_id = Organization.objects.get(user=self.request.user).id
        context['org_id'] = org_id
        return context

    def get_success_url(self):
        blog_id = self.object.pk
        return reverse_lazy('blog_show', kwargs={ 'pk': blog_id })

class BlogDeleteView( LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'blog/show.html'
    success_url = reverse_lazy('blog_index')
