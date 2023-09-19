from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("bands/", views.band_list, name="band_list"),
    path("listings/", views.listing_list, name="listing_list"),
    path("bands/<int:id>", views.band_detail, name="band_detail"),
    path("listings/<int:id>", views.listing_detail, name="listing_detail"),
    path("bands/<int:id>/update/", views.band_update, name="band_update"),
    path("listings/<int:id>/update/", views.listing_update, name="listing_update"),
    path("contact-us/", views.contact, name="contact"),
    path("contact-us/confirmation/", views.confirmation, name="email_sent"),
    path("bands/add/", views.band_create, name="band_create"),
    path("listings/add/", views.listings_create, name="listings_create"),
    path("bands/<int:id>/delete/", views.band_delete, name="band_delete"),
    path("listings/<int:id>/delete/", views.listing_delete, name="listing_delete"),



]
