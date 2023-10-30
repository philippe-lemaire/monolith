from django.shortcuts import render
from .character import Character

# Create your views here.


def generate_character(request):
    return render(
        request,
        template_name="chargen/generate_character.html",
        context={"char": Character()},
    )
