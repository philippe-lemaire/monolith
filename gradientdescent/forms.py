from django import forms
from gamelogic.backgrounds import backgrounds
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class FloorForm(forms.Form):
    floor = forms.IntegerField(min_value=1, max_value=6, initial=1)

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
