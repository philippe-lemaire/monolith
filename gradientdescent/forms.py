from django import forms
from .encounters_per_floor import encounters_per_floor
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class FloorForm(forms.Form):
    choices = [(k, k) for k in encounters_per_floor.keys()]
    floor = forms.ChoiceField(choices=choices)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"

        self.helper.form_action = "gradientdescent:roll_encounters"

        self.helper.add_input(
            Submit(
                "submit",
                "Roll encounter",
                css_class="m-1 btn-secondary",
            )
        )
