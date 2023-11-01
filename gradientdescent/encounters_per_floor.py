from .dice import get_key, roll_d10


encounters_per_floor = {
    "1": {
        0: "1d10 Troubleshooters",
        3: "1d5 Forgotten Androids",
        6: "Distorted corporate muzak plays over the intercom.",
        8: "A Security Android",
        9: "A diver.",
    },
    "2": {
        0: "The Minautor",
        3: "1d5 Chosen Androids",
        6: "1d10 Fallen Androids",
        8: "Ghost in the Machine",
        9: "A diver",
    },
    "3.1": {
        0: "Waste disposal, Save or 1d6 damage",
        3: "1d10 Fallen Androids",
        6: "1d10 Security Androids",
        8: "Ghost in the Machine",
        9: "A diver",
    },
    "3.2": {
        0: "A diver",
        3: "2d10 Bee Drones (p38)",
        6: "1d10 Forgotten Androids",
        8: "1d10 Security Androids",
        9: "Ghost in the Machine",
    },
    "3.3": {
        0: "A diver",
        3: "Silus makes Demands (p40)",
        6: "1d10 Pseudomilk Eels (p42)",
        8: "1d5 Stunted Androids (p41)",
        9: "A Ghost in the Machine",
    },
}
