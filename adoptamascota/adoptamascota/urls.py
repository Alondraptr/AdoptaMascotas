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
from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView
from pet.views import PetListView, PetCreateView, PetDetailView, PetUpdateView, PetDeleteView, OrgListView

from users import views as users_views
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
    path('pet/org', OrgListView.as_view(template_name = "pet/org_pets.html"), name='org_pets'),
    path('pet/<int:pk>', PetDetailView.as_view(template_name = "pet/show.html"), name='pet_show'),
    path('pet/create', PetCreateView.as_view(template_name = "pet/form.html"), name='pet_create'),
    path('pet/edit/<int:pk>', PetUpdateView.as_view(template_name = "pet/form.html"), name='pet_edit'),
    path('pet/delete/<int:pk>', PetDeleteView.as_view(), name='pet_delete'),

    path('blog/', BlogListView.as_view(template_name = "blog/index.html"), name='blog_index'),
    path('blog/<int:pk>', BlogDetailView.as_view(template_name = "blog/show.html"), name='blog_show'),
    path('blog/create', BlogCreateView.as_view(template_name = "blog/form.html"), name='blog_create'),
    path('blog/edit/<int:pk>', BlogUpdateView.as_view(template_name = "blog/form.html"), name='blog_edit'),
    path('blog/delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete'),

    path('accounts/register', users_views.register, name='register'),
    path('accounts/profile', users_views.profile, name='profile'),

    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),

]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

