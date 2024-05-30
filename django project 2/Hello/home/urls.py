from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("index.html", views.index, name='home'),
    path("about.html", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("team.html", views.team, name='team'),
    path("service.html", views.service, name='service'),
    path("why.html", views.why, name='why'),
]
