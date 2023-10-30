backgrounds = [
    "MERCENARY",
    "HUMAN EXPERIMENT",
    "ENGINEER",
    "SMUGGLER",
    "PILOT",
    "MACHINE",
    "UNDERWORLD",
    "PSIONIC",
    "SCIENTIST",
    "SOLDIER",
    "STAR-TOUCHED",
    "BOUNTY HUNTER",
]

dossier_mercenary_part1 = {
    "name": "Signature Weapon",
    "options": {
        1: "<b>Ifriti-9000 “Hell Spitter”</b> (D10 Blast, Thermal, Bulky) and 2 tanks of fuel (spec-ammo). A deluxe model flamethrower that sprays super-thermal plasma that can burn through metal.",
        2: "<b>Folding Vibro-Shank</b> (D6, Deadly, Shock, concealable) A five-inch blade that does absolutely devastating damage. Folds up for concealing. Very-illegal.",
        3: "<b>Supercharged Carbine Repeater</b> (D8 Thermal and d6 Cryo, bulky) Custom modded to switch between thermal or sub-zero energy rounds. Switching takes 1 turn.",
        4: "<b>Jade-Iron Machete (D8, Deadly)</b> 3 feet of marbled green metal with a wicked cutting edge. Expert craftsmanship and quite valuable.",
        5: "<b>“Trusty”</b> (D6 Blaster) & <b>“Rusty”</b> (D6 Blaster, Cheap) These two guns have been with you through thick & thin.",
        6: "<b>“Rusty”</b> (D6 Blaster, Cheap) You used to have two but lost the good one…",
    },
}
dossier_mercenary_part2 = {
    "name": "Old Crew Specialty",
    "options": {
        1: "<b>Para-Military:</b> Private sector military for hire. You were, and probably still are, an absolute professional. Take holo-binocs and a claymore.",
        2: "<b>Seedy Jobs:</b> Hired muscle contracted through criminal syndicates, you are familiar with the less savory parts of the galaxy. Take a grimy outfit, a pack of smokes, & 6d12 worth of underworld trade goods.",
        3: "<b>Ghost Unit:</b> Your crew specialized in delicate matters that needed doing discreetly and without a trace. Take plasti-steel armor (Armor 1, bulky) and a gas mask.",
        4: """<b>Hit Squad:</b> Assassinations were
            your bread & butter. Take a
            thermal detonator, a dark outfit,
            and an infrared visor helm (Armor
            1, heat vision)""",
        5: """<b>Corp-Sec:</b> Private megacorporate
                security for a major faction.
                Generate a faction and NPC and
                determine what type of business.
                Take the talent “Human Shield”.""",
        6: """<b>Deep Cover:</b> Specialists in
            infiltration as double agents for
            espionage and intel gathering.
            Take an auto-lock slicer, drone
            cam, and fake ID.""",
    },
}

dossier_mercenary_part3 = {
    "name": "What happened?",
    "options": {
        1: """<b>Last Man Standing:</b> Something
bad happened and everyone
turned on each other. It was a
bloodbath and you were the last
man standing...at least you think.""",
        2: """<b>Betrayal:</b> Were you the leader, or
were you a betrayer? Or was the
whole crew betrayed by someone
- inside or out? Either way, the
crew broke up and you have to
make your own way.""",
        3: """<b>Things Just Change...:</b> Or maybe
you changed. Either way, you
decided you didn’t want to do
what they did anymore, and
broke off on your own.""",
        4: """<b>Splintered:</b> The group splintered,
maybe from a disagreement in
leadership, or infighting, and
splinter groups broke off.""",
        5: """<b>Kicked Out:</b> Whether it was from
breaking the rules, or not seeing
eye-to-eye with the brass, you
were exiled from your crew on
bad terms.""",
        6: """<b>Left Behind:</b> Things went
sideways on your last mission
and you got left behind mission,
considered MIA or dead. Maybe
it’s time for a fresh start.""",
    },
}

DOSSIERS = {
    "MERCENARY": [
        dossier_mercenary_part1,
        dossier_mercenary_part2,
        dossier_mercenary_part3,
    ],
    "HUMAN EXPERIMENT": [None, None, None],
    "ENGINEER": [None, None, None],
    "SMUGGLER": [None, None, None],
    "PILOT": [None, None, None],
    "MACHINE": [None, None, None],
    "UNDERWORLD": [None, None, None],
    "PSIONIC": [None, None, None],
    "SCIENTIST": [None, None, None],
    "SOLDIER": [None, None, None],
    "STAR-TOUCHED": [None, None, None],
    "BOUNTY HUNTER": [None, None, None],
}
