from django.shortcuts import render

# Create your views here.


def generate_character(request):
    return render(
        request, template_name="generate_character.html", name="generate_character"
    )
