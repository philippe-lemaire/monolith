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

dossier_mercenary = [
    {
        "name": "Signature Weapon",
        "options": {
            1: "<b>Ifriti-9000 “Hell Spitter”</b> (D10 Blast, Thermal, Bulky) and 2 tanks of fuel (spec-ammo). A deluxe model flamethrower that sprays super-thermal plasma that can burn through metal.",
            2: "<b>Folding Vibro-Shank</b> (D6, Deadly, Shock, concealable) A five-inch blade that does absolutely devastating damage. Folds up for concealing. Very-illegal.",
            3: "<b>Supercharged Carbine Repeater</b> (D8 Thermal and d6 Cryo, bulky) Custom modded to switch between thermal or sub-zero energy rounds. Switching takes 1 turn.",
            4: "<b>Jade-Iron Machete (D8, Deadly)</b> 3 feet of marbled green metal with a wicked cutting edge. Expert craftsmanship and quite valuable.",
            5: "<b>“Trusty”</b> (D6 Blaster) & <b>“Rusty”</b> (D6 Blaster, Cheap) These two guns have been with you through thick & thin.",
            6: "<b>“Rusty”</b> (D6 Blaster, Cheap) You used to have two but lost the good one…",
        },
    },
    {
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
    },
    {
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
    },
    ["Old Crew Emblem", "Combat Knife (D6) or 2 Flash Grenades", "Cigar"],
]

dossier_human_experiment = [
    {
        "name": "Side-Effects",
        "options": {
            1: """"<b>Exothermic Lungs:</b> Exhale a superheated spray of plasma (D10 blast, thermal).
Costs 1 fatigue""",
            2: "<b>Magnetism</b> Manipulate metal objects up to 100 lbs with your mind. Costs 1 fatigue.",
            3: "<b>Ghost Skin</b> Willingly phase through solid objects up to 3 feet thick. Costs 1 fatigue.",
            4: """<b>Elasticity</b> Your arms and hands can stretch and change form up to 20 sq feet or 60 feet
in length.""",
            5: "<b>Biomimicry</b> Change or alter your face and skin once a day.",
            6: """<b>Ultra-Conductive</b> You can discharge, locally disrupting all nearby computers and
circuitry once a day. Immune to electricity and EMP damage.""",
        },
    },
    {
        "name": "Type of Experiment",
        "options": {
            1: """<b>Grown in a Tube:</b> You are the
product of scientific brilliance.
You’ve only seen the outside
world while floating inside a vat
of life-sustaining fluid.""",
            2: """<b>Brain Stress:</b> They hooked your
brain up with wires and pushed
your mind to the limits. You know
one random Psionic power.""",
            3: """<b>Nanobot Infusion:</b> Some type
of prototype serum was injected
into your bloodstream. Your
body can naturally heal 1D4 STR
damage a day.""",
            4: """<b>Gene-Splicing:</b> Bio-Engineering
via illegal methods made your
body more hardy and adaptable.
You naturally have 1 armor.""",
            5: """<b>Ghost-Shell:</b> You are a recently
re-animated or unwilling
consciousness implanted into
a synthetic body. You know one
random Astromancy from your
previous life. Your memory is
slowly returning in pieces...""",
            6: """<b>6 Billion Credit Person:</b> You
were a pet project of some
unknown billionaire. They were
attempting to create a perfect
specimen. The project was
considered a partial failure.
Increase one Ability Score to 16.""",
        },
    },
    {
        "name": "How Did You Escape?",
        "options": {
            1: """<b>Violently,</b> by turning your powers
on your captors. Take a bloody
scalpel (D6)""",
            2: """<b>Furtively,</b> you somehow
managed to sneak out in the
dead of night. Take stolen
records worth 4d8 credits on the
black market and notes on how
to find them.""",
            3: """<b>Benevolently,</b> an unknown figure
unlocked your restraints while
nobody was there. When you
woke up, your escape was wide
open. Take a mysterious business
card.""",
            4: """<b>Inexplicably,</b> incomprehensible
quantum displacement shifted
you somewhere completely
random. Take a random weapon
(Roll 1D4). 1-2: small melee, 3:
stun gun, 4: junky blaster.""",
            5: """<b>Compliantly:</b> You didn’t need to
escape, the experiment suddenly
ended and you were released
in the middle of nowhere, with
no way of knowing who had
experimented on you. Your
account now has 2,000 credits as
payment.""",
            6: """<b>Cargo Mix-up:</b> You were being
shipped somewhere and
the manifests got mixed up.
Someone found you and let you
go. The original experimenter is
still looking for you. Take 1D6
random drugs or contraband
items.""",
        },
    },
    # starting gear
    ["Cloak (Hooded)", "Flashlight", "Tattoo (Serial Number or Bar Code)"],
]


dossier_engineer = [
    {
        "name": "Pet Project",
        "options": {
            1: """<b>Dimension De-stabilizer:</b> Tech belt that allows the wearer to slip in and out of reality.
You cannot interact with anything in this reality but are still visible.""",
            2: """<b>Division Multiplier:</b> Harness that when activated splits you into two smaller versions of
yourself. HP & Ability Scores are halved. Inventory exists in a quantum state; items used
by one version are inaccessible to the other. Lasts 1 minute. Causes 1 fatigue.""",
            3: """<b>Molecular Shield Generator:</b> (+1 armor, 3 bonus HP a day) Swarm of fly-sized nanobots
orbit you, occasionally running scans on your biological makeup, providing you with
customized shielding and protection. Bonus HP takes a day to recharge.""",
            4: """<b>Anti-Grav Boots:</b> Activate to reduce your fall speed at the last second and land safely.
Recharge via 100 credit worth of common battery parts in 1d6 hours.""",
            5: """<b>Catherine:</b> An A.I. chip you can implant into any basic device. Currently installed in your
personal comm unit. Catherine is very polite. Will warn you of any imminent danger you
might not notice. May run advanced diagnostics.""",
            6: """<b>Spider-Wasp Drone:</b> A spider-sized drone that can quietly fly, crawl on most surfaces,
and transmit video footage up to 200ft.""",
        },
    },
    {
        "name": "Technical Expertise",
        "options": {
            1: """<b>Cyberware:</b> Take Smart-Eye
implants (Eye Socket.) 10x zoom,
recording & playback.""",
            2: """<b>Starships:</b> You can fix any part of
a ship, but it takes 2D12 hours.""",
            3: """<b>Weapons:</b> Take a Mass Untangler
(D8, illegal, critical damage
instantly disintegrates organics if
they fail a STR save)""",
            4: """<b>Security Systems:</b> You can get
through manually locked doors
and shut down surveillance with
minimal effort and tools.""",
            5: """<b>Robotics:</b> Take a chest harness
(1 slot) with a robotic arm on
it that can carry a weapon and
perform similar actions to your
own arms. Only works with your
DNA signature.""",
            6: """<b>Software:</b> You have increased
effect and reduced failure when
performing tasks related to
computers, hacking, and using
software or user-interfaces.""",
        },
    },
    {
        "name": "Savant Specialty",
        "options": {
            1: """<b>Gearhead:</b> You can spend 1 turn
(10 min) tinkering with most
fist-sized objects you’re familiar
with to get them at least partially
working.""",
            2: """<b>0110101001:</b> You’re oddly
persuasive to A.I. and computing
systems. +1 to reaction roll
results with machines and
synthetics.""",
            3: """<b>MacGyver:</b> You can fix almost
anything with duct tape, holding
anything broken together as if
undamaged for 1D6 hours. Also,
generally handier than almost
anyone else.""",
            4: """<b>Fried Wires:</b> You’ve tinkered with
enough electronic components
that shock damage and anything
electric only damages your
HP, completely ineffective at
damaging your Ability Scores.""",
            5: """<b>Jack of All Trades:</b> You’re
pretty good at everything. Once
a day you can take one fatigue
to accomplish something that
would otherwise require a Save.""",
            6: """<b>Black Lung:</b> Inhaling enough
machine smog has given you a
degree of immunity to inhaled
toxins and other harmful
breathable substances.""",
        },
    },
    # starting gear
    ["Crowbar (D6)", "Duct Tape", "Grease-stained work clothes"],
]
dossier_template = [
    {
        "name": "",
        "options": {
            1: """""",
            2: """""",
            3: """""",
            4: """""",
            5: """""",
            6: """""",
        },
    },
    {
        "name": "",
        "options": {
            1: """""",
            2: """""",
            3: """""",
            4: """""",
            5: """""",
            6: """""",
        },
    },
    {
        "name": "",
        "options": {
            1: """""",
            2: """""",
            3: """""",
            4: """""",
            5: """""",
            6: """""",
        },
    },
    # starting gear
    [],
]

DOSSIERS = {
    "MERCENARY": dossier_mercenary,
    "HUMAN EXPERIMENT": dossier_human_experiment,
    "ENGINEER": dossier_engineer,
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
