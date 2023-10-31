from django.shortcuts import render
from .astromancies import astromancies
from .artefacts import artefacts
from .psionics import psionics

# Create your views here.


def astromancies_view(request):
    template_name = "gamelogic/d66_tables.html"
    context = {"table": astromancies, "h1": "Astromancies"}
    return render(request, template_name, context)


def artefacts_view(request):
    template_name = "gamelogic/d66_tables.html"
    context = {"table": artefacts, "h1": "Artefacts"}
    return render(request, template_name, context)


def psionics_view(request):
    template_name = "gamelogic/d66_tables.html"
    context = {"table": psionics, "h1": "Psionics"}
    return render(request, template_name, context)
