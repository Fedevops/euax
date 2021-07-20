"""projetos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from projects.views import home, form, create, view, edit, update, delete
from activities.views import deletea, edita, homea, forma, creata, updatea, viewa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('form/', form, name='form'),
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('homea/', homea, name='homea'),
    path('forma/', forma, name='form_a'),
    path('creata/', creata, name='creata'),
    path('viewa/<int:pk>/', viewa, name='viewa'),
    path('edita/<int:pk>/', edita, name='edita'),
    path('updatea/<int:pk>/', updatea, name='updatea'),
    path('deletea/<int:pk>/', deletea, name='deletea')
]

