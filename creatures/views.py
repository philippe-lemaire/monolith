import random

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Creature

# Create your views here.


class IndexView(generic.ListView):
    model = Creature
    ordering = ["name"]


class CreatureDetailView(generic.DetailView):
    model = Creature
