from django.urls import path

from . import views

urlpatterns = [
    path("bands/", views.band_list, name="band_list"),
    path("bands/<int:id>", views.band_detail, name="band_detail"),
    path("contact-us/", views.contact, name="contact"),
    path("contact-us/confirmation/", views.confirmation, name="email-sent"),
    path("bands/add/", views.band_create, name="band_create"),


]
