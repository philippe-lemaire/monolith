from django.shortcuts import render
from .dice import (
    roll_d10,
    roll_d100,
    check_doubles,
    doubles_value,
    get_key,
    get_reaction,
)
from .encounters_per_floor import encounters_per_floor
from .forms import FloorForm


# Create your views here.
def roll_encounters_view(request):
    form = FloorForm(request.POST or None)
    context = {"form": form}

    if request.method == "POST":
        if form.is_valid():
            floor = form.cleaned_data["floor"]
            encounters_dict = encounters_per_floor.get(floor)
            encounter_roll = roll_d100()
            encounter_present = check_doubles(encounter_roll)
            context["encounter_present"] = encounter_present
            if encounter_present:
                n = roll_d10()
                distance = doubles_value(encounter_roll)
                key = get_key(n, encounters_dict)
                encounter = encounters_dict[key]
                context["encounter"] = encounter
                context["distance"] = distance
                reaction, status = get_reaction()
                context["reaction"] = reaction
                context["status"] = status

    return render(request, "gradientdescent/roll_encounters.html", context)
