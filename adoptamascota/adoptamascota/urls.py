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
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from organization.views import OrganizationListView, OrganizationCreateView, OrganizationDetailView, OrganizationUpdateView, OrganizationDeleteView
#from organization import views as organization_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('organization/', OrganizationListView.as_view(template_name = "organization/index.html"), name='index'),
    path('organization/<int:pk>', OrganizationDetailView.as_view(template_name = "organization/show.html"), name='show'),
    #path('organization/create', organization_views.create, name='create'),
    path('organization/create', OrganizationCreateView.as_view(template_name = "organization/form.html"), name='create'),
    path('organization/edit/<int:pk>', OrganizationUpdateView.as_view(template_name = "organization/form.html"), name='edit'),
    path('organization/delete/<int:pk>', OrganizationDeleteView.as_view(), name='delete'),

    path('', views.index),
    path('adopta/', views.adopta),
    path('blog/', views.blog),
   # path('registro/', views.registro),
   # path('ingreso/', views.ingreso),
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

