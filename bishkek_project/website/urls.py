from django.contrib import admin
from django.urls import path, include
from .views import index, about, contact




urlpatterns = [
    path("", index, name='home'),
    path("about/", about, name='about'),
    path("contact/", contact, name='contact'),
]