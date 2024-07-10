from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.Name, name='Name'),
    path("helloworld/", views.helloworld, name='helloworld'),
    path("Profile/", views.profile, name='profile'),
    path("contacts/", views.contacts, name='contacts'),
    path("abouts/", views.abouts, name='abouts')
]