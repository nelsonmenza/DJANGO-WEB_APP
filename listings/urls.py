from django.urls import path

from . import views

urlpatterns = [
    path("bands/", views.band_list, name="band_list"),
    path("bands/<int:id>", views.band_detail, name="band_detail"),

]
