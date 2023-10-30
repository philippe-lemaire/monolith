from gamelogic.roll import roll
from gamelogic.backgrounds import backgrounds, DOSSIERS
from gamelogic.finishing_touches import (
    physique,
    mannerisms,
    hair,
    clothing_style,
    face,
    male_names,
    female_names,
    ambiguous_names,
    last_names,
)
from random import choice


class Character:
    def __init__(self):
        self.first_name = choice(choice((male_names, female_names, ambiguous_names)))
        self.last_name = choice(last_names)
        self.STR = roll("3d6")
        self.DEX = roll("3d6")
        self.WIL = roll("3d6")
        self.HP = roll("d6")

        self.background = choice(backgrounds)

        (
            self.dossier_part1,
            self.dossier_part2,
            self.dossier_part3,
            self.gear,
            self.profile,
        ) = DOSSIERS.get(self.background)
        self.dossier_name = self.dossier_part1.get("name")
        self.dossier_option = self.dossier_part1.get("options").get(self.HP)
        self.dossier_subpart_name = self.dossier_part2.get("name")
        self.dossier_subpart_option = choice(
            list(self.dossier_part2.get("options").values())
        )
        self.dossier_question = self.dossier_part3.get("name")
        self.dossier_answer = choice(list(self.dossier_part3.get("options").values()))
        self.common_gear = [
            "Three days of rations (one slot)",
            "Cheap Data-comm (one slot)",
            "Glo-torch (one slot)",
            f"{roll('3d6')} Credits (C)",
        ]
        self.finishing_touches = {
            "physique": choice(physique),
            "mannerism": choice(mannerisms),
            "hair": choice(hair),
            "clothing style": choice(clothing_style),
            "face": choice(face),
        }
