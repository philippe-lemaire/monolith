from django.urls import path

from . import views

app_name = "gamelogic"

urlpatterns = [
    path("astromancies", views.astromancies_view, name="astromancies"),
    path("artefacts", views.artefacts_view, name="artefacts"),
    path("psionics", views.psionics_view, name="psionics"),
]
