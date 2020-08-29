from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name='home'),
    path("me", views.me, name='me'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("tracker", views.tracker, name='tracker'),
    path("checkout", views.checkout, name='checkout'),

]
