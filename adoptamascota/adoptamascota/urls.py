"""adoptamascota URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from organization.views import OrganizationListView, OrganizationCreateView, OrganizationDetailView, OrganizationUpdateView, OrganizationDeleteView
from pet.views import PetListView, PetCreateView, PetDetailView, PetUpdateView, PetDeleteView

#from organization import views as organization_views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('organization/', OrganizationListView.as_view(template_name = "organization/index.html"), name='org_index'),
    path('organization/<int:pk>', OrganizationDetailView.as_view(template_name = "organization/show.html"), name='org_show'),
    #path('organization/create', organization_views.create, name='create'),
    path('organization/create', OrganizationCreateView.as_view(template_name = "organization/form.html"), name='org_create'),
    path('organization/edit/<int:pk>', OrganizationUpdateView.as_view(template_name = "organization/form.html"), name='org_edit'),
    path('organization/delete/<int:pk>', OrganizationDeleteView.as_view(), name='org_delete'),

    path('pet/', PetListView.as_view(template_name = "pet/index.html"), name='pet_index'),
    path('pet/<int:pk>', PetDetailView.as_view(template_name = "pet/show.html"), name='pet_show'),
    path('pet/create', PetCreateView.as_view(template_name = "pet/form.html"), name='pet_create'),
    path('pet/edit/<int:pk>', PetUpdateView.as_view(template_name = "pet/form.html"), name='pet_edit'),
    path('pet/delete/<int:pk>', PetDeleteView.as_view(), name='pet_delete'),

    path('', views.index),
    path('blog/', views.blog),
    path('registro/', views.registro),
    path('ingreso/', views.ingreso),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

