import json, os

OUT = "/mnt/user-data/outputs/bestiary_jsons"
os.makedirs(OUT, exist_ok=True)

CR = 7
XP = 2900
PROF = 3

def make_char(name, faction, race, alignment, size, armor_type, armor_class,
              hit_die_num, hit_die_size, speed, ability_scores,
              saving_throws_prof, skills_list,
              damage_vulns, damage_res, damage_imm, condition_imm,
              senses, languages,
              additional_abilities, actions, reactions,
              legendary_actions_desc="", legendary_actions=None,
              description="", environment=""):
    if legendary_actions is None:
        legendary_actions = []
    mods = {k: (v - 10) // 2 for k, v in ability_scores.items()}
    am = {"strength":"Str","dexterity":"Dex","constitution":"Con","intelligence":"Int","wisdom":"Wis","charisma":"Cha"}
    as_strs = {}
    for k, v in ability_scores.items():
        m = mods[k]
        s = f"+{m}" if m >= 0 else str(m)
        as_strs[k] = f"{v} ({s})"
    st_list = []
    for ab in ["strength","dexterity","constitution","intelligence","wisdom","charisma"]:
        prof = ab in saving_throws_prof
        mod = mods[ab] + (PROF if prof else 0)
        s = f"+{mod}" if mod >= 0 else str(mod)
        st_list.append({"ability": ab, "proficient": prof, "modifier": mod, "modifierStr": f"{am[ab]} {s}"})
    skill_ability = {
        "Athletics":"strength","Acrobatics":"dexterity","Sleight of Hand":"dexterity","Stealth":"dexterity",
        "Arcana":"intelligence","History":"intelligence","Investigation":"intelligence","Nature":"intelligence","Religion":"intelligence",
        "Animal Handling":"wisdom","Insight":"wisdom","Medicine":"wisdom","Perception":"wisdom","Survival":"wisdom",
        "Deception":"charisma","Intimidation":"charisma","Performance":"charisma","Persuasion":"charisma"
    }
    sk_list = []
    for sk_name in skills_list:
        ab = skill_ability.get(sk_name, "wisdom")
        mod = mods[ab] + PROF
        s = f"+{mod}" if mod >= 0 else str(mod)
        sk_list.append({"name": sk_name, "proficient": True, "modifier": mod, "modifierStr": f"{sk_name} {s}"})
    con_bonus = mods["constitution"] * hit_die_num
    avg_die = (hit_die_size + 1) // 2
    hp = hit_die_num * avg_die + con_bonus
    if con_bonus >= 0:
        hp_str = f"{hp} ({hit_die_num}d{hit_die_size} + {con_bonus})"
    else:
        hp_str = f"{hp} ({hit_die_num}d{hit_die_size} - {abs(con_bonus)})"
    passive = 10 + mods["wisdom"] + (PROF if "Perception" in skills_list else 0)
    obj = {
        "flavor": {"faction": faction, "environment": environment, "description": description,
                   "nameIsProper": True, "imageUrl": "", "descriptionHtml": {}},
        "stats": {
            "size": size, "race": race, "alignment": alignment, "armorType": armor_type,
            "armorClass": armor_class, "numHitDie": hit_die_num, "speed": speed,
            "abilityScores": ability_scores, "proficiencyBonus": PROF,
            "damageVulnerabilities": damage_vulns, "damageResistances": damage_res,
            "damageImmunities": damage_imm, "conditionImmunities": condition_imm,
            "senses": senses, "languages": languages,
            "challengeRating": CR, "experiencePoints": XP,
            "legendaryActionsPerRound": 0, "legendaryActionsDescription": legendary_actions_desc,
            "savingThrows": st_list, "skills": sk_list,
            "additionalAbilities": additional_abilities, "actions": actions, "reactions": reactions,
            "legendaryActions": legendary_actions, "hitDieSize": hit_die_size,
            "armorTypeStr": f"({armor_type})", "abilityScoreModifiers": mods,
            "abilityScoreStrs": as_strs, "extraHealthFromConstitution": con_bonus,
            "hitPoints": hp, "hitPointsStr": hp_str,
            "legendaryActionsDescriptionHtml": {}, "passivePerception": passive,
            "challengeRatingStr": str(CR)
        },
        "sharing": {"linkSharingEnabled": False},
        "name": name
    }
    fname = name.replace(' ', '_').replace('/', '_').replace("'", "")
    with open(f"{OUT}/{fname}.json", "w") as f:
        json.dump(obj, f, indent=2)
    print(f"  {fname}.json")

def ab(n, desc): return {"name": n, "description": desc, "descriptionHtml": {}}
def act(n, desc): return {"name": n, "description": desc, "descriptionHtml": {}}
def rx(n, desc): return {"name": n, "description": desc, "descriptionHtml": {}}

print("Team Birdbrains:")
make_char("Kutaka Niwatari","Team Birdbrains","Fey (Chicken Deity)","neutral good","Small","Natural Armor",15,9,8,"30 ft., Fly 40 ft.",
    {"strength":12,"dexterity":16,"constitution":16,"intelligence":12,"wisdom":18,"charisma":16},
    ["wisdom","charisma"],["Perception","Animal Handling","Religion"],[],[],[],["Frightened"],
    ["darkvision 60 ft."],["Common","Sylvan"],
    [ab("Keeper of the Gateway","Kutaka has advantage on Wisdom (Perception) checks and cannot be surprised. She knows the exact HP total and CR of any Undead creature she can see."),
     ab("Soul Shepherd","When a creature is reduced to 0 HP within 30 feet of Kutaka, she can use a free action to grant it one death saving throw immediately, before it falls unconscious.")],
    [act("Multiattack","Kutaka makes two Talon Strike attacks."),
     act("Talon Strike","<i>Melee Weapon Attack:</i> +7 to hit, reach 5 ft., one target. <i>Hit:</i> 14 (2d10 + 3) Piercing damage."),
     act("Heaven's Gate Edict (Recharge 5-6)","Kutaka calls forth a radiant proclamation in a 20-foot radius. Each creature must make a DC 15 Wisdom saving throw or take 28 (8d6) Radiant damage and be Stunned until the end of their next turn. On a success, half damage only.")],
    [rx("Divine Intercept","When a creature within 30 feet of Kutaka would drop to 0 HP, she can use her reaction to halve the triggering damage. If this keeps the creature alive, it has 1 HP instead.")],
    description="Guardian of the Boundary Between Life and Death",environment="Mountain")

print("\nTeam Upside Down:")
make_char("Shinmyoumaru Sukuna","Team Upside Down","Humanoid (Inchling)","neutral good","Tiny","Natural Armor",14,9,6,"20 ft.",
    {"strength":8,"dexterity":18,"constitution":14,"intelligence":14,"wisdom":12,"charisma":18},
    ["dexterity","charisma"],["Sleight of Hand","Acrobatics","Persuasion"],[],[],[],["Charmed"],
    ["darkvision 30 ft."],["Common"],
    [ab("Miracle Mallet","Once per turn, Shinmyoumaru can choose to either double or halve the size of one creature or object she can see within 30 feet (no save). This lasts until the end of her next turn. A doubled creature gains +2 to melee attack rolls and damage; a halved creature has disadvantage on Strength checks and saving throws."),
     ab("Inchling Evasion","Shinmyoumaru has advantage on Dexterity saving throws. When she succeeds on a Dexterity saving throw, she takes no damage from that effect.")],
    [act("Multiattack","Shinmyoumaru makes two Needle Rapier attacks."),
     act("Needle Rapier","<i>Melee Weapon Attack:</i> +7 to hit, reach 5 ft., one target. <i>Hit:</i> 11 (2d6 + 4) Piercing damage. If Shinmyoumaru has advantage on the roll, the target must make a DC 15 Dexterity saving throw or be Restrained until the end of its next turn."),
     act("Mallet Burst (Recharge 5-6)","Shinmyoumaru swings her miracle mallet, releasing a burst of wish-energy in a 15-foot radius. Each creature must make a DC 15 Charisma saving throw or take 28 (8d6) Force damage. On a success, half damage only.")],
    [rx("Size Shift","When Shinmyoumaru is hit by an attack, she can use her reaction to suddenly shrink. The attack's damage is halved, and she can move up to 10 feet without provoking opportunity attacks.")],
    description="Wielder of the Miracle Mallet")

make_char("Benben Tsukumo","Team Upside Down","Undead (Tsukumogami)","chaotic neutral","Medium","Natural Armor",14,10,8,"30 ft.",
    {"strength":8,"dexterity":16,"constitution":14,"intelligence":14,"wisdom":10,"charisma":20},
    ["charisma","dexterity"],["Performance","Deception","Stealth"],
    [],["necrotic"],["poison"],["Poisoned","Frightened"],["darkvision 60 ft."],["Common"],
    [ab("Chord Resonance","When Benben deals Thunder or Psychic damage, she can choose one additional creature within 10 feet of the target. That creature takes 7 (2d6) Thunder damage as the sound reverberates."),
     ab("Undying Instrument","If Benben is reduced to 0 HP, she can make a DC 13 Charisma saving throw. On a success, she rises with 1 HP at the start of her next turn. She can use this once per long rest.")],
    [act("Multiattack","Benben makes two String Lash attacks."),
     act("String Lash","<i>Melee Weapon Attack:</i> +6 to hit, reach 10 ft., one target. <i>Hit:</i> 16 (2d12 + 3) Thunder damage."),
     act("Discordant Requiem (Recharge 5-6)","Benben plays a soul-shaking dirge. Each creature within 30 feet must make a DC 16 Wisdom saving throw or take 35 (10d6) Psychic damage and be Frightened of Benben until the end of its next turn. On a success, half damage only.")],
    [rx("Resonant Counter","When a creature hits Benben with a melee attack, she can use her reaction to deal 11 (2d10) Thunder damage to that creature.")],
    description="Animated Biwa of Restless Song")

make_char("Sekibanki","Team Upside Down","Undead (Rokurokubi)","chaotic neutral","Medium","Natural Armor",15,10,8,"30 ft. (head: Fly 40 ft.)",
    {"strength":10,"dexterity":18,"constitution":14,"intelligence":14,"wisdom":12,"charisma":16},
    ["dexterity","charisma"],["Stealth","Deception","Intimidation"],
    [],["necrotic","bludgeoning, piercing, and slashing from nonmagical attacks"],[],["Frightened"],
    ["darkvision 60 ft."],["Common"],
    [ab("Detachable Head","Sekibanki can detach her head as a bonus action. While detached, her head has its own movement (fly 40 ft.) and can make Eyebeam attacks independently. Her body continues to act but can only make Melee Claw attacks. Both share HP. The head can reattach as a bonus action."),
     ab("Nine Lives","Sekibanki has advantage on death saving throws.")],
    [act("Multiattack","Sekibanki makes two Claw attacks, or one Claw and one Eyebeam."),
     act("Claw","<i>Melee Weapon Attack:</i> +7 to hit, reach 5 ft., one target. <i>Hit:</i> 13 (2d8 + 4) Slashing damage."),
     act("Eyebeam","<i>Ranged Spell Attack:</i> +6 to hit, range 60 ft., one target. <i>Hit:</i> 21 (6d6) Necrotic damage."),
     act("Head Flock (Recharge 5-6)","Sekibanki launches multiple head-copies in a 20-foot radius. Each creature must make a DC 15 Dexterity saving throw or take 35 (10d6) Necrotic damage. On a success, half damage only.")],
    [rx("Severed Dodge","When Sekibanki's head is detached and targeted by an attack, she can fly her head up to 20 feet. If this takes it out of range, the attack misses.")],
    description="The Headless Youkai of Dual Bodies")

print("\nTeam Dark Eater:")
make_char("Clownpiece","Team Dark Eater","Fiend (Fairy)","chaotic evil","Small","Natural Armor",15,10,8,"35 ft., Fly 40 ft.",
    {"strength":10,"dexterity":18,"constitution":16,"intelligence":10,"wisdom":8,"charisma":20},
    ["dexterity","charisma"],["Performance","Intimidation","Stealth"],
    [],["fire","necrotic"],["poison"],["Poisoned","Charmed","Frightened"],["darkvision 120 ft."],["Common","Infernal"],
    [ab("Lunatic Flame","When Clownpiece deals Fire damage, she can have it bypass resistance but not immunity. Creatures failing a save against her fire effects are also Frightened until the end of their next turn."),
     ab("Hell Fairy's Madness","At the start of each of Clownpiece's turns, each creature within 10 feet must succeed on a DC 16 Wisdom saving throw or take the Confused condition until the start of its next turn.")],
    [act("Multiattack","Clownpiece makes two Torch Jab attacks."),
     act("Torch Jab","<i>Melee Weapon Attack:</i> +7 to hit, reach 5 ft., one target. <i>Hit:</i> 9 (2d4 + 4) Piercing damage plus 9 (2d8) Fire damage."),
     act("Hell Torch Barrage (Recharge 5-6)","Clownpiece hurls hellfire in a 30-foot cone. Each creature must make a DC 16 Dexterity saving throw or take 21 (6d6) Fire damage plus 21 (6d6) Psychic damage. On a success, half damage only.")],
    [rx("Infernal Counterflare","When Clownpiece takes damage, each creature within 5 feet of her takes 14 (4d6) Fire damage.")],
    description="Hell Fairy of Lunatic Flames",environment="Planar (Hell)")

make_char("Yamame Kurodani","Team Dark Eater","Monstrosity (Tsuchigumo)","chaotic good","Medium","Natural Armor",16,10,10,"35 ft., Climb 35 ft.",
    {"strength":18,"dexterity":16,"constitution":18,"intelligence":12,"wisdom":12,"charisma":14},
    ["strength","constitution"],["Athletics","Intimidation","Stealth"],
    [],["poison"],["poison"],["Poisoned"],["darkvision 60 ft., tremorsense 30 ft."],["Common","Undercommon"],
    [ab("Web Walker","Yamame ignores movement restrictions caused by webbing and difficult terrain of earth or stone. She can move along walls and ceilings without checks."),
     ab("Disease Carrier","Creatures failing a save against Yamame's Venom Weave contract a disease. At the end of each of their turns until cured (DC 15 Constitution save), they take 7 (2d6) Poison damage and have disadvantage on Constitution saving throws.")],
    [act("Multiattack","Yamame makes one Bite and one Slam, or two Slams."),
     act("Bite","<i>Melee Weapon Attack:</i> +7 to hit, reach 5 ft., one target. <i>Hit:</i> 14 (2d10 + 3) Piercing damage plus 14 (2d10 + 3) Poison damage. DC 16 Constitution save or Poisoned for 1 minute."),
     act("Slam","<i>Melee Weapon Attack:</i> +7 to hit, reach 5 ft., one target. <i>Hit:</i> 17 (2d12 + 4) Bludgeoning damage."),
     act("Venom Weave (Recharge 5-6)","A 20-foot radius of venomous webbing (range 60 ft.). DC 16 Strength save or Restrained and take 28 (8d6) Poison damage. On success, half, not Restrained.")],
    [rx("Silk Cushion","When Yamame is hit by a ranged attack, she spins a web shield, reducing damage by 11 (2d10).")],
    description="Beautiful Spider Youkai of the Former Capital",environment="Underground")

print("\nTeam Scarlet Masters:")
make_char("Sakuya Izayoi","Team Scarlet Masters","Humanoid (Human)","lawful neutral","Medium","Natural Armor",17,10,8,"35 ft.",
    {"strength":12,"dexterity":22,"constitution":14,"intelligence":16,"wisdom":16,"charisma":14},
    ["dexterity","intelligence"],["Stealth","Perception","Sleight of Hand","Acrobatics"],[],[],[],[],
    ["darkvision 30 ft."],["Common"],
    [ab("Time Stop","Once per short rest, Sakuya stops time as a free action. She immediately takes an additional full turn before current initiative resumes. During this extra turn, no other creature can take reactions."),
     ab("Perfect and Elegant Maid","Sakuya's thrown knife attacks ignore cover and half-cover. She can attack creatures she cannot see as long as she has heard them this turn.")],
    [act("Multiattack","Sakuya makes three Silver Knife attacks."),
     act("Silver Knife","<i>Ranged Weapon Attack:</i> +9 to hit, range 20/60 ft., one target. <i>Hit:</i> 13 (2d6 + 6) Piercing damage. If two or more knives hit the same target in one turn, that target is Slowed until end of its next turn."),
     act("Knife Storm (Recharge 5-6)","A barrage of knives in a 30-foot cone. DC 17 Dexterity save or 35 (10d6) Piercing damage. On success, half.")],
    [rx("Temporal Redirect","When a creature within 30 feet is hit by an attack, Sakuya alters the timestream — the attack misses instead. Once per short rest.")],
    description="The Perfect and Elegant Maid of the Scarlet Devil Mansion")

make_char("Hong Meiling","Team Scarlet Masters","Humanoid (Youkai)","neutral","Medium","Unarmored Defense",16,10,10,"35 ft.",
    {"strength":20,"dexterity":16,"constitution":18,"intelligence":10,"wisdom":14,"charisma":12},
    ["strength","constitution"],["Athletics","Perception","Acrobatics"],
    [],["bludgeoning, piercing, and slashing from nonmagical attacks"],[],[],["darkvision 60 ft."],["Common"],
    [ab("Martial Artist","Meiling's unarmed strikes count as magical. When she makes an unarmed strike as part of the Attack action, she can make one additional unarmed strike as a bonus action."),
     ab("Chi Flow","At the start of each of Meiling's turns, she regains 7 (2d6) HP if she has at least 1 HP and has not taken Radiant or Necrotic damage since her last turn.")],
    [act("Multiattack","Meiling makes two Fist of the Gatekeeper attacks and one Kick."),
     act("Fist of the Gatekeeper","<i>Melee Weapon Attack:</i> +8 to hit, reach 5 ft., one target. <i>Hit:</i> 14 (2d8 + 5) Bludgeoning damage."),
     act("Kick","<i>Melee Weapon Attack:</i> +8 to hit, reach 5 ft., one target. <i>Hit:</i> 16 (2d10 + 5) Bludgeoning damage. DC 16 Strength save or knocked Prone and pushed 10 feet."),
     act("Colorful Rain (Recharge 5-6)","A burst of rainbow chi in a 20-foot radius. DC 16 Constitution save or 28 (8d6) Radiant damage and Stunned until end of next turn. On success, half.")],
    [rx("Iron Gate Block","When Meiling is hit by a melee attack, she reduces the damage by 16 (2d10 + 5).")],
    description="Colorful Guardian of the Scarlet Devil Mansion Gate")

make_char("Flandre Scarlet","Team Scarlet Masters","Undead (Vampire)","chaotic neutral","Small","Natural Armor",17,11,8,"30 ft., Fly 50 ft.",
    {"strength":20,"dexterity":18,"constitution":18,"intelligence":14,"wisdom":10,"charisma":18},
    ["strength","dexterity"],["Perception","Stealth","Intimidation"],
    [],["necrotic","bludgeoning, piercing, and slashing from nonmagical attacks"],["poison"],["Poisoned","Charmed","Frightened"],
    ["darkvision 120 ft."],["Common"],
    [ab("Destruction Instinct","Once per turn, Flandre can destroy the 'eye' of one creature within 30 feet. The creature makes a DC 16 Constitution saving throw or takes 35 (10d6) Force damage (on success, 17 (5d6))."),
     ab("Sunlight Sensitivity","In sunlight, Flandre has disadvantage on attack rolls and Perception checks relying on sight."),
     ab("Regeneration","Flandre regains 10 HP at the start of her turn if she has at least 1 HP and hasn't taken Radiant damage since her last turn.")],
    [act("Multiattack","Flandre makes two Claw attacks."),
     act("Claw","<i>Melee Weapon Attack:</i> +8 to hit, reach 5 ft., one target. <i>Hit:</i> 14 (2d8 + 5) Slashing damage plus 7 (2d6) Necrotic damage."),
     act("Forbidden Barrage (Recharge 5-6)","A chaotic explosion in a 30-foot radius. DC 16 Dexterity save or 21 (6d6) Fire plus 21 (6d6) Force damage. On success, half.")],
    [rx("Evasive Flap","When Flandre is hit by an attack, she can fly up to 15 feet. If this takes her out of reach, the attack's damage is halved.")],
    description="The Imprisoned Little Devil of the Scarlet Mansion")

make_char("Patchouli Knowledge","Team Scarlet Masters","Humanoid (Magician)","neutral","Medium","Natural Armor",14,11,6,"20 ft.",
    {"strength":8,"dexterity":10,"constitution":14,"intelligence":22,"wisdom":16,"charisma":14},
    ["intelligence","wisdom"],["Arcana","History","Religion","Investigation"],[],[],[],["Charmed"],
    ["darkvision 60 ft."],["Common","Elvish","Infernal","Celestial"],
    [ab("One-Week Girl","Patchouli can cast two spells in the same turn if both deal different damage types. Spell attacks +9, save DC 17."),
     ab("Elemental Mastery","Patchouli's damage spells can be changed to any of: Fire, Cold, Lightning, Thunder, Acid, or Radiant at will.")],
    [act("Elemental Blast","<i>Ranged Spell Attack:</i> +9 to hit, range 90 ft., one target. <i>Hit:</i> 28 (5d8 + 6) damage of her chosen type."),
     act("Royal Flare (Recharge 5-6)","A solar explosion in a 30-foot radius. DC 17 Dexterity save or 21 (6d6) Fire plus 21 (6d6) Radiant damage. On success, half.")],
    [rx("Elemental Counter","When a creature within 60 feet casts a spell, Patchouli makes one Elemental Blast against that creature.")],
    description="The Unmoving Great Library")

print("\nTeam Your Lie in April:")
make_char("Daiyousei","Team Your Lie in April","Fey (Fairy)","neutral good","Small","Natural Armor",14,10,8,"30 ft., Fly 50 ft.",
    {"strength":10,"dexterity":18,"constitution":14,"intelligence":14,"wisdom":16,"charisma":18},
    ["wisdom","charisma"],["Perception","Medicine","Persuasion"],
    [],["radiant"],[],["Charmed","Frightened"],["darkvision 60 ft."],["Common","Sylvan"],
    [ab("Greater Fairy's Light","Daiyousei sheds bright light 20 ft., dim 40 ft. Undead in the bright light have disadvantage on attack rolls. She can toggle this as a bonus action."),
     ab("Healing Sparkle","As a bonus action, Daiyousei touches a creature to restore 14 (4d6) HP. Uses equal to Wisdom modifier (3) per long rest.")],
    [act("Multiattack","Daiyousei makes two Fairy Lance attacks."),
     act("Fairy Lance","<i>Ranged Spell Attack:</i> +7 to hit, range 60 ft., one target. <i>Hit:</i> 18 (4d8) Radiant damage."),
     act("Blessing of Light (Recharge 5-6)","A wave of healing light in a 30-foot radius. Allied creatures regain 21 (6d6) HP. Hostile creatures make DC 15 Wisdom save or take 21 (6d6) Radiant damage.")],
    [rx("Fairy Shield","When an ally within 30 feet is hit by an attack, Daiyousei grants that ally +4 AC against the triggering attack, potentially causing a miss.")],
    description="The Greater Fairy of the Misty Lake",environment="Forest")

make_char("Yatsuhashi Tsukumo","Team Your Lie in April","Undead (Tsukumogami)","chaotic neutral","Medium","Natural Armor",14,10,8,"30 ft.",
    {"strength":10,"dexterity":14,"constitution":14,"intelligence":14,"wisdom":12,"charisma":20},
    ["charisma","wisdom"],["Performance","Insight","Deception"],
    [],["necrotic"],["poison"],["Poisoned","Frightened"],["darkvision 60 ft."],["Common"],
    [ab("Memory Erasure","When Yatsuhashi hits a creature, it makes a DC 16 Wisdom save or forgets the last minute of events — losing her location if hidden, forgetting concentration tracking, and unable to use reactions triggered by her until end of its next turn."),
     ab("Koto Resonance","If Benben Tsukumo is within 60 feet and alive, all Thunder and Psychic damage both deal is increased by 1d6.")],
    [act("Multiattack","Yatsuhashi makes two String Sweep attacks."),
     act("String Sweep","<i>Melee Weapon Attack:</i> +8 to hit, reach 10 ft., one target. <i>Hit:</i> 16 (2d10 + 5) Thunder damage."),
     act("Forced Melody (Recharge 5-6)","A haunting chord in a 30-foot radius. DC 16 Wisdom save or 35 (10d6) Psychic damage and forget Yatsuhashi is hostile until end of next turn. On success, half.")],
    [rx("Amnesia Strike","When a creature misses Yatsuhashi, it makes a DC 16 Wisdom save or immediately forgets the attack, losing its action for this turn.")],
    description="Memory-Erasing Koto Tsukumogami")

make_char("Tsukasa Kudamaki","Team Your Lie in April","Fey (Fox Spirit)","neutral evil","Medium","Natural Armor",15,10,8,"35 ft.",
    {"strength":10,"dexterity":18,"constitution":14,"intelligence":18,"wisdom":14,"charisma":18},
    ["intelligence","charisma"],["Deception","Arcana","Stealth","Persuasion"],[],[],[],["Charmed"],
    ["darkvision 60 ft."],["Common","Sylvan"],
    [ab("Fox Fire Manipulation","Tsukasa creates up to 3 foxfire motes as a bonus action (dim light 10 ft. each). She can detonate one as a bonus action (range 30 ft.): DC 16 Dex save or 9 (2d8) Fire damage."),
     ab("Tool Spirit Manipulation","Tsukasa communicates telepathically with Tsukumogami within 60 feet and issues simple commands as a bonus action.")],
    [act("Multiattack","Tsukasa makes two Foxfire Bolt attacks."),
     act("Foxfire Bolt","<i>Ranged Spell Attack:</i> +7 to hit, range 60 ft., one target. <i>Hit:</i> 18 (4d8) Fire damage."),
     act("Tsukumogami Summoning (Recharge 5-6)","Tsukasa summons three Animated Objects (Small or Medium) that act on her initiative, OR releases a foxfire explosion in a 20-foot radius: DC 16 Dex save or 28 (8d6) Fire damage (half on success).")],
    [rx("Foxfire Screen","When Tsukasa is targeted by a ranged spell attack, she creates a screen of foxfire, imposing disadvantage on the attack roll.")],
    description="Fox Spirit Manipulator of Tool Souls")

make_char("Parsee Mizuhashi","Team Your Lie in April","Fey (Hashihime)","chaotic neutral","Medium","Natural Armor",15,10,8,"30 ft.",
    {"strength":12,"dexterity":18,"constitution":14,"intelligence":14,"wisdom":12,"charisma":18},
    ["dexterity","charisma"],["Insight","Deception","Intimidation"],[],[],[],["Charmed"],
    ["darkvision 60 ft."],["Common","Undercommon"],
    [ab("Green-Eyed Curse","When a creature within 30 feet scores a critical hit or kills, Parsee can react to impose a jealousy curse: disadvantage on attacks against Parsee and 7 (2d6) Psychic damage at start of its turns for 1 minute (DC 15 Cha save ends each turn)."),
     ab("Envy Mirror","When Parsee takes damage from a creature within 30 feet, she reflects half as Psychic damage (no save).")],
    [act("Multiattack","Parsee makes two Envy Shard attacks."),
     act("Envy Shard","<i>Ranged Spell Attack:</i> +7 to hit, range 60 ft., one target. <i>Hit:</i> 18 (4d8) Psychic damage."),
     act("Jealousy Bloom (Recharge 5-6)","A flood of envy in a 20-foot radius. DC 16 Wisdom save or 35 (10d6) Psychic damage and Charmed (treats all allies as enemies) until end of next turn. On success, half.")],
    [rx("Jealous Reflection","When a creature within 30 feet casts a buff or healing spell on another, Parsee replicates the effect on herself or an ally.")],
    description="The Green-Eyed Jealousy Youkai of the Bridge",environment="Underground")

print("\nTeam Celestial Crashers:")
make_char("Joon Yorigami","Team Celestial Crashers","Humanoid (God of Poverty)","chaotic evil","Medium","Natural Armor",15,10,8,"35 ft.",
    {"strength":12,"dexterity":18,"constitution":14,"intelligence":16,"wisdom":10,"charisma":22},
    ["dexterity","charisma"],["Deception","Persuasion","Sleight of Hand"],[],[],[],["Charmed","Frightened"],
    ["darkvision 60 ft."],["Common"],
    [ab("Divine Plunder","When Joon hits a creature, she can drain one resource: it loses one use of its most recently recovered ability or spell slot. Twice per short rest."),
     ab("Poverty Aura","Creatures within 10 feet have disadvantage on saves against Charmed or Frightened, and their healing effects are halved.")],
    [act("Multiattack","Joon makes two Poverty Strike attacks."),
     act("Poverty Strike","<i>Melee Weapon Attack:</i> +7 to hit, reach 5 ft., one target. <i>Hit:</i> 14 (2d8 + 5) Force damage. DC 17 Charisma save or disadvantage on next attack roll."),
     act("Ruin's Fortune (Recharge 5-6)","A wave of ruin in a 30-foot radius. DC 17 Charisma save or 35 (10d6) Force damage and lose one use of their most powerful rechargeable ability. On success, half.")],
    [rx("Steal the Win","When a creature within 30 feet regains HP, Parsee redirects half that healing to herself instead.")],
    description="The God of Poverty and Ruination")

make_char("Watatsuki no Toyohime","Team Celestial Crashers","Celestial (Lunarian)","lawful neutral","Medium","Natural Armor",16,12,8,"35 ft.",
    {"strength":14,"dexterity":18,"constitution":16,"intelligence":18,"wisdom":18,"charisma":18},
    ["wisdom","intelligence"],["Perception","Arcana","History","Insight"],
    [],["radiant","bludgeoning, piercing, and slashing from nonmagical attacks"],[],["Charmed","Frightened"],
    ["darkvision 120 ft."],["Common","Celestial"],
    [ab("Lunar Authority","Advantage on saves against spells. Spells of 3rd level or lower have no effect on Toyohime."),
     ab("Boundary of Moon and Sea","Once per turn when Toyohime hits a creature, she can teleport it up to 30 feet to an unoccupied space (no save).")],
    [act("Multiattack","Toyohime makes two Lunar Fan attacks."),
     act("Lunar Fan","<i>Ranged Spell Attack:</i> +8 to hit, range 60 ft., one target. <i>Hit:</i> 22 (4d10) Radiant damage."),
     act("Moon Tide Devastation (Recharge 5-6)","A surge of moon-sea energy in a 10-foot radius (range 90 ft.). DC 17 Dexterity save or 28 (8d6) Radiant plus 14 (4d6) Cold damage and knocked Prone. On success, half.")],
    [rx("Lunar Ward","When an allied creature within 30 feet is hit, Toyohime grants it resistance to the damage.")],
    description="Princess of the Moon and Sea")

make_char("Toyosatomimi no Miko","Team Celestial Crashers","Celestial (Saint)","lawful neutral","Medium","Natural Armor",16,12,8,"35 ft.",
    {"strength":12,"dexterity":16,"constitution":16,"intelligence":20,"wisdom":18,"charisma":22},
    ["wisdom","charisma"],["Insight","History","Persuasion","Religion"],
    [],["radiant"],[],["Charmed","Frightened"],["darkvision 60 ft."],["Common","Celestial"],
    [ab("Ten Desires","Miko knows the general motivation of any creature she can see. Creatures with hidden intentions must succeed on a DC 18 Charisma save or she sees through them."),
     ab("Shotgun Kaen","Once per short rest, when Miko takes her Attack action she also fires divine swords in a 15-foot cone: DC 17 Dexterity save or 28 (8d6) Radiant damage (half on success).")],
    [act("Multiattack","Miko makes two Sword of Desires attacks."),
     act("Sword of Desires","<i>Ranged Spell Attack:</i> +9 to hit, range 60 ft., one target. <i>Hit:</i> 21 (3d10 + 5) Radiant damage."),
     act("Divine Edict (Recharge 5-6)","A divine proclamation in a 30-foot radius. DC 18 Wisdom save or 35 (10d6) Radiant damage and Stunned until end of next turn. On success, half.")],
    [rx("Prescient Parry","When Miko is targeted by an attack, she adds +5 to her AC against it, having perceived the attacker's desire.")],
    description="The Saint of Ten Desires")

make_char("Tenshi Hinanawi","Team Celestial Crashers","Celestial (Celestial Being)","chaotic good","Medium","Natural Armor",18,12,10,"35 ft., Fly 40 ft.",
    {"strength":22,"dexterity":16,"constitution":20,"intelligence":12,"wisdom":12,"charisma":16},
    ["strength","constitution"],["Athletics","Perception","Intimidation"],
    [],["bludgeoning, piercing, and slashing from nonmagical attacks","lightning","thunder"],[],["Frightened"],
    ["darkvision 60 ft."],["Common","Celestial"],
    [ab("Sword of Hisou","Tenshi's melee attacks deal +7 (2d6) damage: Radiant vs Celestials, Undead, and Fiends; Lightning vs others."),
     ab("Keystones of Heaven","As a bonus action, Tenshi summons a keystone (up to 3 max). Keystones create difficult terrain. Entering or starting a turn on one deals 7 (2d6) Bludgeoning damage.")],
    [act("Multiattack","Tenshi makes two Sword of Hisou attacks."),
     act("Sword of Hisou","<i>Melee Weapon Attack:</i> +9 to hit, reach 5 ft., one target. <i>Hit:</i> 20 (2d12 + 7) Slashing damage plus 7 (2d6) Lightning or Radiant damage."),
     act("Earthquake (Recharge 5-6)","Tenshi slams her blade down in a 30-foot radius. DC 17 Strength save or 35 (10d6) Bludgeoning damage and knocked Prone. Area becomes difficult terrain for 1 minute. On success, half.")],
    [rx("Rock Solid","When Tenshi is hit by an attack, she halves the damage and cannot be moved, knocked Prone, or displaced.")],
    description="The Eldest Daughter of the Hinanawi Celestials",environment="Celestial Realm")

print("\nTeam Oni Punch Gals:")
make_char("Yuugi Hoshiguma","Team Oni Punch Gals","Humanoid (Oni)","chaotic good","Large","Natural Armor",18,12,12,"40 ft.",
    {"strength":24,"dexterity":12,"constitution":22,"intelligence":12,"wisdom":12,"charisma":16},
    ["strength","constitution"],["Athletics","Intimidation"],
    [],["bludgeoning, piercing, and slashing from nonmagical attacks"],[],["Frightened","Charmed"],
    ["darkvision 60 ft."],["Common"],
    [ab("Undeniable Strength","Yuugi's melee attacks are magical. She has advantage on Strength checks and saves and cannot be knocked Prone unless she chooses."),
     ab("One-Horned Oni","When Yuugi takes damage, she gains a Strength Charge (max 3). She can spend one as a bonus action to add 14 (4d6) damage to her next melee attack.")],
    [act("Multiattack","Yuugi makes two Fist Strike attacks."),
     act("Fist Strike","<i>Melee Weapon Attack:</i> +10 to hit, reach 10 ft., one target. <i>Hit:</i> 24 (3d10 + 8) Bludgeoning damage."),
     act("Shockwave Stomp (Recharge 5-6)","A 30-foot radius tremor. DC 18 Strength save or 42 (12d6) Bludgeoning damage and knocked Prone. On success, half.")],
    [rx("Four Devas Counter","When a creature hits Yuugi with a melee attack, she immediately makes one Fist Strike against it.")],
    description="The Legendary Oni of the Former Capital",environment="Underground")

make_char("Suika Ibuki","Team Oni Punch Gals","Humanoid (Oni)","chaotic neutral","Small","Natural Armor",16,12,10,"35 ft., Fly 30 ft.",
    {"strength":22,"dexterity":14,"constitution":20,"intelligence":12,"wisdom":10,"charisma":18},
    ["strength","constitution"],["Athletics","Intimidation","Perception"],
    [],["bludgeoning, piercing, and slashing from nonmagical attacks"],[],["Charmed","Frightened","Poisoned"],
    ["darkvision 60 ft."],["Common"],
    [ab("Density Manipulation","As a bonus action, Suika shifts between: Dense Form (AC +3, speed -10, melee +2d6 damage) or Mist Form (AC -3, speed +20, can move through creatures)."),
     ab("Mist Reassembly","When Suika drops to 0 HP, she disperses and reforms at start of next turn with 14 HP within 30 feet. Once per long rest.")],
    [act("Multiattack","Suika makes two Gourd Slam attacks."),
     act("Gourd Slam","<i>Melee Weapon Attack:</i> +9 to hit, reach 5 ft., one target. <i>Hit:</i> 19 (2d12 + 6) Bludgeoning damage."),
     act("Missing Power (Recharge 5-6)","An explosion in a 20-foot radius. DC 17 Strength save or 42 (12d6) Bludgeoning damage, pushed 20 ft., knocked Prone. On success, half.")],
    [rx("Density Surge","When Suika takes damage, she instantly enters Dense Form and adds 14 (4d6) to her next attack's damage this turn.")],
    description="The Tiny Oni of the Four Celestial Kings",environment="Planar")

make_char("Zanmu Nippaku","Team Oni Punch Gals","Humanoid (Oni)","lawful neutral","Medium","Natural Armor",16,12,10,"35 ft.",
    {"strength":20,"dexterity":14,"constitution":20,"intelligence":16,"wisdom":18,"charisma":14},
    ["strength","wisdom"],["Athletics","Insight","Religion"],
    [],["necrotic","bludgeoning, piercing, and slashing from nonmagical attacks"],[],["Charmed","Frightened"],
    ["darkvision 60 ft.", "truesight 30 ft."],["Common","Infernal"],
    [ab("Hell's Authority","Oni and lesser undead within 30 feet must make a DC 16 Wisdom save at start of their turns or move toward Zanmu and take no actions."),
     ab("Soul Rend","When Zanmu kills a creature, she gains 14 (4d6) temporary HP and her next attack deals +14 (4d6) Necrotic damage.")],
    [act("Multiattack","Zanmu makes two Hell Claw attacks."),
     act("Hell Claw","<i>Melee Weapon Attack:</i> +8 to hit, reach 5 ft., one target. <i>Hit:</i> 18 (2d12 + 5) Slashing damage plus 9 (2d8) Necrotic damage."),
     act("Oni Dominion (Recharge 5-6)","Zanmu exerts authority in a 30-foot radius. Oni and Undead are affected automatically. Others: DC 16 Wisdom save or 35 (10d6) Necrotic damage and Paralyzed until end of next turn. On success, half.")],
    [rx("Fearless Riposte","When Zanmu is hit by a melee attack, she makes one Hell Claw attack against the attacker.")],
    description="Empress of Hell and Ruler of the Oni",environment="Planar (Hell)")

make_char("Kasen Ibaraki","Team Oni Punch Gals","Humanoid (Oni/Hermit)","neutral","Medium","Natural Armor",16,12,8,"35 ft.",
    {"strength":18,"dexterity":14,"constitution":18,"intelligence":16,"wisdom":20,"charisma":16},
    ["strength","wisdom"],["Athletics","Perception","Animal Handling","Medicine"],
    [],["bludgeoning, piercing, and slashing from nonmagical attacks"],[],["Charmed","Frightened"],
    ["darkvision 60 ft."],["Common","Celestial"],
    [ab("Hermit's Discipline","Kasen cannot be moved against her will unless she fails a Strength save. Advantage on saves against Incapacitated and Stunned."),
     ab("Dragon Arm","Once per short rest as a bonus action, Kasen unleashes her draconic arm: one Dragon Arm Strike dealing 21 (6d6) Bludgeoning damage (DC 17 Strength save or flung 30 ft. and knocked Prone).")],
    [act("Multiattack","Kasen makes two Hermit's Fist attacks."),
     act("Hermit's Fist","<i>Melee Weapon Attack:</i> +7 to hit, reach 5 ft., one target. <i>Hit:</i> 16 (2d10 + 5) Bludgeoning damage."),
     act("Animal Summons (Recharge 5-6)","Kasen summons 2 Giant Eagles or 1 Giant Ape acting on her initiative for 1 minute, OR releases a chi blast in a 20-foot radius: DC 17 Wisdom save or 35 (10d6) Radiant damage (half on success).")],
    [rx("Disciplined Counter","When a creature misses Kasen with a melee attack, she makes one Hermit's Fist attack against it.")],
    description="The Horned Hermit of Calamity",environment="Mountain")

print("\nTeam Golden Sun:")
make_char("Nazrin","Team Golden Sun","Humanoid (Youkai)","neutral","Small","Natural Armor",14,10,6,"35 ft.",
    {"strength":10,"dexterity":20,"constitution":14,"intelligence":16,"wisdom":18,"charisma":12},
    ["dexterity","wisdom"],["Perception","Investigation","Stealth","Acrobatics"],[],[],[],[],
    ["darkvision 60 ft.", "tremorsense 30 ft."],["Common","Elvish"],
    [ab("Dowsing Rods","Nazrin always knows the direction to the nearest unattended valuable within 1 mile. In combat, she detects magical items on creatures within 60 feet as a bonus action."),
     ab("Mouse Swarm","Once per short rest as a bonus action, a swarm of mice attacks one creature within 30 feet. DC 15 Dexterity save or 14 (4d6) Piercing damage and disadvantage on next attack roll.")],
    [act("Multiattack","Nazrin makes three Dowsing Rod Lash attacks."),
     act("Dowsing Rod Lash","<i>Melee Weapon Attack:</i> +8 to hit, reach 10 ft., one target. <i>Hit:</i> 12 (2d6 + 5) Bludgeoning damage."),
     act("Treasure Finding Wave (Recharge 5-6)","A divination pulse in a 30-foot radius. DC 16 Wisdom save or 35 (10d6) Force damage and all held/worn items glow golden (negating invisibility for those items). On success, half.")],
    [rx("Nimble Escape","When Nazrin is hit by an attack, she moves up to 15 feet without provoking opportunity attacks.")],
    description="The Mouse Youkai and Dowser of Treasures",environment="Mountain")

make_char("Shou Toramaru","Team Golden Sun","Humanoid (Youkai/Avatar)","lawful good","Medium","Natural Armor",16,12,8,"35 ft.",
    {"strength":18,"dexterity":14,"constitution":18,"intelligence":14,"wisdom":18,"charisma":18},
    ["strength","wisdom"],["Athletics","Religion","Perception"],
    [],["lightning"],[],["Charmed","Frightened"],["darkvision 60 ft."],["Common","Celestial"],
    [ab("Vessel of Bishamonten","Shou is the avatar of the god of war. Weapon attacks are magical and deal +7 (2d6) Lightning damage. Advantage on saves against Frightened."),
     ab("Pagoda of Life","At the start of each of Shou's turns, one allied creature within 30 feet (her choice) regains 7 (2d6) HP.")],
    [act("Multiattack","Shou makes two Tiger Spear attacks."),
     act("Tiger Spear","<i>Melee Weapon Attack:</i> +7 to hit, reach 10 ft., one target. <i>Hit:</i> 18 (2d12 + 5) Piercing damage plus 7 (2d6) Lightning damage."),
     act("Star Maelstrom (Recharge 5-6)","A burst of divine lightning in a 30-foot radius. DC 16 Dexterity save or 21 (6d6) Lightning plus 21 (6d6) Radiant damage and knocked Prone. On success, half.")],
    [rx("Divine Interception","When an allied creature within 30 feet is hit, Shou moves up to 15 feet toward it. If she ends in the attacker's reach, she makes one Tiger Spear attack.")],
    description="Avatar of the God of War and Treasure")

make_char("Byakuren Hijiri","Team Golden Sun","Humanoid (Magician/Saint)","neutral good","Medium","Natural Armor",17,12,8,"35 ft.",
    {"strength":14,"dexterity":14,"constitution":16,"intelligence":18,"wisdom":18,"charisma":22},
    ["wisdom","charisma"],["Religion","Insight","Persuasion","Athletics"],
    [],["bludgeoning, piercing, and slashing from nonmagical attacks","necrotic"],[],["Charmed","Frightened"],
    ["darkvision 60 ft."],["Common","Celestial","Infernal"],
    [ab("Buddha's Blessing","Byakuren and allies within 30 feet have advantage on death saving throws. When an ally within 30 feet would drop to 0, Byakuren can react to grant them 14 (4d6) temporary HP instead."),
     ab("Witch's Body","Melee attacks deal +7 (2d6) Force damage. Byakuren is proficient with all weapons.")],
    [act("Multiattack","Byakuren makes two Scroll Slam attacks."),
     act("Scroll Slam","<i>Melee Weapon Attack:</i> +7 to hit, reach 5 ft., one target. <i>Hit:</i> 16 (2d10 + 5) Bludgeoning damage plus 7 (2d6) Force damage."),
     act("Holy Barrage (Recharge 5-6)","A wave of divine light in a 30-foot radius. Enemy creatures: DC 18 Wisdom save or 35 (10d6) Radiant damage and Blinded until end of next turn. Allied creatures in area regain 21 (6d6) HP.")],
    [rx("Intercessory Grace","When an allied creature within 30 feet fails a saving throw, Byakuren grants it a reroll, using the better result.")],
    description="The Magician-Saint of Myouren Temple")

make_char("Sunny Milk","Team Golden Sun","Fey (Fairy)","chaotic neutral","Small","Natural Armor",14,10,8,"30 ft., Fly 50 ft.",
    {"strength":8,"dexterity":18,"constitution":14,"intelligence":14,"wisdom":12,"charisma":18},
    ["dexterity","charisma"],["Stealth","Perception","Acrobatics"],
    [],["radiant"],[],[],["darkvision 60 ft."],["Common","Sylvan"],
    [ab("Light Refraction","As a bonus action, Sunny bends light around herself or an ally within 30 feet, granting Invisibility until start of her next turn."),
     ab("Sunlight Amplifier","Sunny's Radiant damage ignores resistance and deals maximum damage in areas of bright natural sunlight.")],
    [act("Multiattack","Sunny makes three Sunbeam attacks."),
     act("Sunbeam","<i>Ranged Spell Attack:</i> +7 to hit, range 60 ft., one target. <i>Hit:</i> 16 (4d6 + 2) Radiant damage."),
     act("Prism Flare (Recharge 5-6)","A blinding explosion in a 20-foot radius. DC 16 Constitution save or 35 (10d6) Radiant damage and Blinded until end of next turn. On success, half.")],
    [rx("Refracted Dodge","When targeted by an attack, Sunny bends light around herself, imposing disadvantage on the triggering roll.")],
    description="The Sunlight Fairy of Light Refraction",environment="Forest")

print("\nTeam Ghostly Apparitions:")
make_char("Shion Yorigami","Team Ghostly Apparitions","Fiend (God of Poverty)","chaotic neutral","Medium","Natural Armor",14,10,8,"30 ft.",
    {"strength":8,"dexterity":16,"constitution":14,"intelligence":12,"wisdom":12,"charisma":20},
    ["charisma","dexterity"],["Deception","Stealth","Perception"],
    [],[],["poison"],["Poisoned","Charmed"],["darkvision 60 ft."],["Common","Infernal"],
    [ab("Poverty Miasma","Creatures starting their turn within 15 feet must succeed on DC 16 Charisma save or take 7 (2d6) Necrotic damage and have disadvantage on ability checks and attacks until their next turn."),
     ab("Bad Luck Aura","Creatures within 30 feet cannot benefit from luck-rerolling abilities. Critical hits they make become normal hits instead.")],
    [act("Multiattack","Shion makes two Misfortune Touch attacks."),
     act("Misfortune Touch","<i>Melee Weapon Attack:</i> +6 to hit, reach 5 ft., one target. <i>Hit:</i> 14 (2d10 + 3) Necrotic damage. DC 16 Charisma save or disadvantage on its next saving throw."),
     act("Ruination Wave (Recharge 5-6)","Poverty energy in a 20-foot radius. DC 16 Charisma save or 35 (10d6) Necrotic damage and lose all temporary HP. On success, half.")],
    [rx("Poverty Redirect","When Shion would take damage, she redirects half to one creature within 30 feet (no save).")],
    description="The Impoverished God of Misfortune")

make_char("Chiyari Tenkajin","Team Ghostly Apparitions","Undead (Gashadokuro)","chaotic neutral","Large","Natural Armor",17,12,10,"40 ft.",
    {"strength":22,"dexterity":10,"constitution":20,"intelligence":8,"wisdom":10,"charisma":12},
    ["strength","constitution"],["Athletics","Intimidation"],
    [],["necrotic","bludgeoning, piercing, and slashing from nonmagical attacks"],["poison"],
    ["Poisoned","Frightened","Exhaustion"],["darkvision 60 ft."],["Common","Infernal"],
    [ab("Skull Terror","When Chiyari enters combat, each creature within 30 feet must succeed on DC 16 Wisdom save or be Frightened for 1 minute. Repeat save at end of each turn."),
     ab("Undying Hunger","Chiyari has advantage on melee attack rolls against creatures below half their HP maximum.")],
    [act("Multiattack","Chiyari makes two Bone Crush attacks."),
     act("Bone Crush","<i>Melee Weapon Attack:</i> +9 to hit, reach 10 ft., one target. <i>Hit:</i> 22 (3d10 + 6) Bludgeoning damage. DC 17 Strength save or Grappled (escape DC 17)."),
     act("Death Rattle (Recharge 5-6)","A bone-rattling shriek in a 30-foot radius. DC 16 Constitution save or 35 (10d6) Necrotic damage and one level of Exhaustion. On success, half, no Exhaustion.")],
    [rx("Bone Shield","When Chiyari is hit by a melee attack, it deals half damage as she interposes skeletal limbs.")],
    description="The Gashadokuro of Insatiable Hunger")

make_char("Soga no Tojiko","Team Ghostly Apparitions","Undead (Gaki)","chaotic neutral","Medium","Natural Armor",14,10,8,"30 ft., Fly 40 ft.",
    {"strength":12,"dexterity":16,"constitution":14,"intelligence":14,"wisdom":14,"charisma":18},
    ["charisma","dexterity"],["Intimidation","Stealth","Perception"],
    [],["thunder","necrotic"],["poison","lightning"],["Poisoned","Frightened","Charmed"],
    ["darkvision 60 ft."],["Common"],
    [ab("Thunder Ghost","Tojiko can pass through walls and objects. She cannot end her turn inside them. Non-magical physical attacks cannot hit her while she is moving through solid matter."),
     ab("Vengeful Lightning","Once per turn when Tojiko hits a creature, she calls a ghostly bolt dealing +14 (4d6) Lightning damage (no save).")],
    [act("Multiattack","Tojiko makes two Thunder Shock attacks."),
     act("Thunder Shock","<i>Ranged Spell Attack:</i> +7 to hit, range 60 ft., one target. <i>Hit:</i> 18 (4d8) Thunder damage plus 7 (2d6) Necrotic damage."),
     act("Wrath of the Dead (Recharge 5-6)","A ghost-thunder storm in a 30-foot radius. DC 16 Dexterity save or 21 (6d6) Thunder plus 21 (6d6) Necrotic damage and Stunned until end of next turn. On success, half.")],
    [rx("Phase Shift","When targeted by an attack, Tojiko becomes incorporeal until start of next turn: resistance to non-magical damage, immune to grapple and restrain.")],
    description="The Vengeful Spirit of Lightning and Thunder")

make_char("Mizuchi Miyadeguchi","Team Ghostly Apparitions","Monstrosity (Serpent God)","neutral evil","Large","Natural Armor",17,12,12,"35 ft., Swim 50 ft.",
    {"strength":22,"dexterity":14,"constitution":20,"intelligence":14,"wisdom":16,"charisma":16},
    ["strength","constitution"],["Athletics","Perception","Intimidation"],
    [],["poison","cold"],["poison"],["Poisoned","Frightened"],
    ["darkvision 60 ft.", "blindsight 30 ft."],["Common","Draconic"],
    [ab("Serpentine Grace","Advantage on saves against knocked Prone. Ignores movement penalty in mud and marsh."),
     ab("Curse of the River","When Mizuchi's Bite hits, the target is Cursed for 1 minute: disadvantage on Strength and Dexterity saves. Removed by Greater Restoration.")],
    [act("Multiattack","Mizuchi makes one Bite and one Tail Slam."),
     act("Bite","<i>Melee Weapon Attack:</i> +9 to hit, reach 10 ft., one target. <i>Hit:</i> 19 (2d12 + 6) Piercing plus 14 (4d6) Poison damage. DC 17 Constitution save or Poisoned 1 minute."),
     act("Tail Slam","<i>Melee Weapon Attack:</i> +9 to hit, reach 15 ft., one target. <i>Hit:</i> 24 (4d8 + 6) Bludgeoning damage. DC 17 Strength save or knocked Prone."),
     act("Flood Surge (Recharge 5-6)","A cursed torrent in a 30-ft. line, 10 ft. wide. DC 17 Strength save or 35 (10d6) Bludgeoning plus 14 (4d6) Cold damage, pushed 20 ft., knocked Prone. On success, half.")],
    [rx("Serpent's Coil","When a creature within 10 feet misses Mizuchi with a melee attack, she attempts to Grapple it (escape DC 17).")],
    description="The Ancient River Serpent God of Curses",environment="Waterways")

print("\nTeam Prismriver Ensemble:")
make_char("Lunasa Prismriver","Team Prismriver Ensemble","Undead (Poltergeist)","neutral","Medium","Natural Armor",13,10,8,"30 ft., Fly 40 ft.",
    {"strength":8,"dexterity":14,"constitution":14,"intelligence":14,"wisdom":12,"charisma":20},
    ["charisma","wisdom"],["Performance","Insight","Perception"],
    [],["necrotic"],["poison"],["Poisoned","Frightened"],["darkvision 60 ft."],["Common"],
    [ab("Melancholy Strings","Creatures within 30 feet who can hear Lunasa make DC 16 Wisdom saves at the start of their turns or become Saddened (disadvantage on attacks, no opportunity attacks until end of turn). Constructs and deafened creatures immune."),
     ab("Phantom Violin","Lunasa controls her violin telekinetically within 30 feet and cannot be disarmed of it.")],
    [act("Multiattack","Lunasa makes two Phantom Bow attacks."),
     act("Phantom Bow","<i>Ranged Spell Attack:</i> +8 to hit, range 60 ft., one target. <i>Hit:</i> 21 (3d10 + 5) Necrotic damage."),
     act("Requiem for the Living (Recharge 5-6)","A funeral dirge in a 30-foot radius. Creatures that can hear make DC 16 Wisdom save or 35 (10d6) Necrotic damage and Incapacitated until end of next turn. On success, half.")],
    [rx("Sorrow Counter","When a creature succeeds on Lunasa's Melancholy Strings save, she can impose disadvantage on its next attack roll.")],
    description="Eldest Prismriver, Poltergeist Violinist of Melancholy")

make_char("Merlin Prismriver","Team Prismriver Ensemble","Undead (Poltergeist)","chaotic good","Medium","Natural Armor",13,10,8,"30 ft., Fly 40 ft.",
    {"strength":8,"dexterity":16,"constitution":14,"intelligence":12,"wisdom":10,"charisma":20},
    ["charisma","dexterity"],["Performance","Acrobatics","Persuasion"],
    [],["necrotic"],["poison"],["Poisoned","Charmed","Frightened"],["darkvision 60 ft."],["Common"],
    [ab("Euphoric Trumpet","When Merlin plays, allied creatures within 30 feet gain Bardic Inspiration (1d8) at the start of each of their turns."),
     ab("Phantom Trumpet","Merlin controls her trumpet telekinetically and cannot be disarmed.")],
    [act("Multiattack","Merlin makes two Sonic Bolt attacks."),
     act("Sonic Bolt","<i>Ranged Spell Attack:</i> +8 to hit, range 60 ft., one target. <i>Hit:</i> 19 (3d8 + 5) Thunder damage."),
     act("Fanfare of Joy (Recharge 5-6)","An ecstatic blast in a 30-foot radius. Enemies that can hear: DC 16 Wisdom save or 35 (10d6) Psychic damage and Charmed until end of next turn. Allies in area gain 21 (6d6) temporary HP.")],
    [rx("Rallying Note","When an allied creature within 30 feet fails a saving throw, Merlin lets it reroll, keeping the better result.")],
    description="Youngest Prismriver, Poltergeist Trumpeter of Euphoria")

make_char("Lyrica Prismriver","Team Prismriver Ensemble","Undead (Poltergeist)","neutral","Medium","Natural Armor",13,10,8,"30 ft., Fly 40 ft.",
    {"strength":8,"dexterity":16,"constitution":14,"intelligence":16,"wisdom":14,"charisma":20},
    ["charisma","intelligence"],["Performance","Arcana","Deception"],
    [],["necrotic"],["poison"],["Poisoned","Frightened"],["darkvision 60 ft."],["Common"],
    [ab("Fantasia Keys","When Lyrica hits a creature, it makes DC 16 Wisdom save or is confused as to the source of sound (disadvantage on Perception checks relying on hearing) for 1 minute."),
     ab("Phantom Piano","Lyrica controls her piano telekinetically and cannot be disarmed.")],
    [act("Multiattack","Lyrica makes two Key Strike attacks."),
     act("Key Strike","<i>Ranged Spell Attack:</i> +8 to hit, range 60 ft., one target. <i>Hit:</i> 18 (4d6 + 4) Thunder plus 7 (2d6) Psychic damage."),
     act("Phantom Ensemble (Recharge 5-6)","A phantom concert in a 30-foot radius. DC 16 Wisdom save or 28 (8d6) Psychic plus 14 (4d6) Thunder damage and Stunned until end of next turn. On success, half.")],
    [rx("Dissonant Chord","When a creature within 60 feet casts a spell, Lyrica forces DC 16 Wisdom save or the caster takes 14 (4d6) Psychic damage and loses concentration.")],
    description="Middle Prismriver, Poltergeist Pianist of Illusion")

make_char("Raiko Horikawa","Team Prismriver Ensemble","Undead (Tsukumogami)","chaotic good","Medium","Natural Armor",15,10,8,"35 ft.",
    {"strength":16,"dexterity":16,"constitution":16,"intelligence":12,"wisdom":14,"charisma":18},
    ["charisma","dexterity"],["Performance","Athletics","Intimidation"],
    [],["lightning","thunder"],["poison"],["Poisoned"],["darkvision 60 ft."],["Common"],
    [ab("Living Rhythm","At the start of each of Raiko's turns, each allied creature within 30 feet gains +2 to their next attack roll or saving throw (fades after use or Raiko's next turn)."),
     ab("Thunder Heart","When Raiko takes Lightning or Thunder damage, she is healed for half the amount instead.")],
    [act("Multiattack","Raiko makes two Drumstrike attacks."),
     act("Drumstrike","<i>Melee Weapon Attack:</i> +6 to hit, reach 5 ft., one target. <i>Hit:</i> 16 (2d12 + 3) Thunder damage."),
     act("Thunderous Solo (Recharge 5-6)","A shockwave in a 30-foot radius. DC 16 Constitution save or 42 (12d6) Thunder damage and Deafened for 1 minute. On success, half, not Deafened.")],
    [rx("Beat Drop","When Raiko is hit by an attack, she beats her drums — each creature within 5 feet takes 11 (2d10) Thunder damage.")],
    description="The Thunder Drum Tsukumogami")

print("\nTeam Yakumo:")
make_char("Yukari Yakumo","Team Yakumo","Fey (Youkai Sage)","neutral","Medium","Natural Armor",18,14,8,"35 ft., Fly 60 ft.",
    {"strength":12,"dexterity":18,"constitution":18,"intelligence":24,"wisdom":20,"charisma":22},
    ["wisdom","intelligence"],["Arcana","Perception","History","Insight"],
    [],["bludgeoning, piercing, and slashing from nonmagical attacks"],[],["Charmed","Frightened","Sleep"],
    ["truesight 60 ft."],["Common","Sylvan","Celestial","Infernal","Deep Speech"],
    [ab("Boundary Manipulation","Once per turn as a free action, Yukari opens a gap to teleport herself or one creature within 60 feet to any unoccupied space she can see (DC 19 Wisdom save for unwilling). She can also attack from any direction through a gap."),
     ab("Youkai Sage","Yukari cannot be surprised. She knows when any creature within 60 feet uses a magical ability. She casts any cantrip as a free action once per turn.")],
    [act("Multiattack","Yukari makes two Gap Claw attacks."),
     act("Gap Claw","<i>Melee Weapon Attack:</i> +10 to hit, reach 5 ft. (or any range via gap), one target. <i>Hit:</i> 21 (3d10 + 5) Slashing plus 11 (2d10) Force damage."),
     act("Yukari's Boundary (Recharge 5-6)","Boundary manipulation in a 20-foot radius. DC 19 Intelligence save or 35 (10d6) Force damage, teleported to a random space within 60 feet, and Stunned until end of next turn. On success, half.")],
    [rx("Gap Shield","When Yukari is targeted by a ranged attack or spell, she opens a gap, redirecting it to any creature she can see within 60 feet.")],
    description="The Youkai of Boundaries and the Great Sage of Gensokyo")

make_char("Chen","Team Yakumo","Fey (Nekomata)","chaotic good","Small","Natural Armor",16,10,8,"40 ft., Fly 40 ft.",
    {"strength":14,"dexterity":22,"constitution":14,"intelligence":10,"wisdom":14,"charisma":14},
    ["dexterity","charisma"],["Acrobatics","Stealth","Perception"],[],[],[],[],
    ["darkvision 60 ft."],["Common","Sylvan"],
    [ab("Two-Tailed Cat","Advantage on Dexterity (Acrobatics). Cannot fall prone unless willing. Always lands on feet; no fall damage from 60 ft. or less."),
     ab("Shikigami Speed","Speed increases by 10 ft. when Chen starts her turn without having taken damage since last turn. Dash as a bonus action.")],
    [act("Multiattack","Chen makes three Claw Slash attacks."),
     act("Claw Slash","<i>Melee Weapon Attack:</i> +9 to hit, reach 5 ft., one target. <i>Hit:</i> 13 (2d6 + 6) Slashing damage."),
     act("Nekomata Frenzy (Recharge 5-6)","Chen dashes through up to 5 creatures within 30 feet. DC 17 Dexterity save or 35 (10d6) Slashing damage. On success, half.")],
    [rx("Nimble Pounce","When a creature misses an attack against Chen or an ally within 30 feet, she moves up to 15 feet toward it and makes one Claw Slash.")],
    description="Ran's Shikigami, the Nekomata of Gensokyo")

make_char("Ran Yakumo","Team Yakumo","Fey (Kitsune)","neutral","Medium","Natural Armor",17,12,8,"40 ft., Fly 50 ft.",
    {"strength":16,"dexterity":18,"constitution":18,"intelligence":22,"wisdom":18,"charisma":18},
    ["intelligence","wisdom"],["Arcana","Insight","Perception","History"],
    [],["bludgeoning, piercing, and slashing from nonmagical attacks"],[],["Charmed"],
    ["truesight 30 ft.", "darkvision 60 ft."],["Common","Sylvan","Celestial"],
    [ab("Nine-Tailed Fox","Advantage on Intelligence and Wisdom saves. Immune to Charmed and magical sleep."),
     ab("Shikigami Calculation","Cannot be surprised. Advantage on initiative. At start of combat, knows one weakness (vulnerability, immunity, or trait) of each visible creature.")],
    [act("Multiattack","Ran makes two Fox Fire attacks, or one Fox Fire and one Tail Whip."),
     act("Fox Fire","<i>Ranged Spell Attack:</i> +9 to hit, range 60 ft., one target. <i>Hit:</i> 21 (3d10 + 5) Fire damage."),
     act("Tail Whip","<i>Melee Weapon Attack:</i> +7 to hit, reach 10 ft., one target. <i>Hit:</i> 18 (2d12 + 5) Bludgeoning damage. DC 17 Strength save or knocked Prone and pushed 10 feet."),
     act("Fox's Reckoning (Recharge 5-6)","A magical barrage in a 20-foot radius. DC 18 Intelligence save or 35 (10d6) Force plus 14 (4d6) Fire damage and unable to use bonus actions until end of next turn. On success, half.")],
    [rx("Calculation Counter","When a creature within 60 feet casts a spell, Ran and all allies within 30 feet have advantage on the resulting saving throw.")],
    description="Yukari's Shikigami, the Nine-Tailed Fox")

print("\nTeam True Terror:")
make_char("Koishi Komeiji","Team True Terror","Humanoid (Satori)","chaotic neutral","Small","Natural Armor",16,10,8,"35 ft., Fly 35 ft.",
    {"strength":8,"dexterity":20,"constitution":14,"intelligence":10,"wisdom":6,"charisma":22},
    ["charisma","dexterity"],["Stealth","Deception","Acrobatics"],[],[],[],["Charmed","Frightened"],
    ["truesight 30 ft.", "darkvision 60 ft."],["Common"],
    [ab("Closed Eye","Koishi cannot be targeted by mind-reading or emotion-detection abilities. Creatures cannot gain the Frightened condition from noticing her, and she never triggers readied actions or reactions unless already targeted this turn."),
     ab("Subconscious Strike","Once per turn, Koishi has advantage on her first attack roll. If this attack hits, it is also a critical hit.")],
    [act("Multiattack","Koishi makes two Subconscious Touch attacks."),
     act("Subconscious Touch","<i>Melee Weapon Attack:</i> +8 to hit, reach 5 ft., one target. <i>Hit:</i> 14 (2d8 + 5) Psychic damage. DC 17 Wisdom save or unable to perceive Koishi until end of next turn."),
     act("Super Ego (Recharge 5-6)","Koishi reaches into all minds in a 30-foot radius. DC 17 Wisdom save or 35 (10d6) Psychic damage and Stunned until end of next turn. On success, half.")],
    [rx("Instinctive Dodge","When Koishi would be hit by an attack, it misses automatically. Uses equal to Charisma modifier (5) per long rest.")],
    description="The Girl Who Closed Her Third Eye and Became Unnoticed",environment="Underground")

make_char("Nue Houjuu","Team True Terror","Monstrosity (Nue)","chaotic neutral","Medium","Natural Armor",16,10,8,"30 ft., Fly 60 ft.",
    {"strength":14,"dexterity":20,"constitution":16,"intelligence":16,"wisdom":12,"charisma":18},
    ["dexterity","charisma"],["Stealth","Deception","Intimidation"],[],[],[],["Frightened"],
    ["truesight 60 ft.", "darkvision 60 ft."],["Common"],
    [ab("Unidentified Form","Nue can alter her appearance or any object she touches as a bonus action. Creatures seeing through it (DC 16 Insight) take 14 (4d6) Psychic damage. Spells/abilities targeting her must succeed on DC 16 Intelligence check or fail."),
     ab("Seeds of Unknown Form","As a bonus action (range 30 ft.), Nue plants uncertainty. DC 16 Wisdom save or the creature perceives all allies as enemies until end of its next turn.")],
    [act("Multiattack","Nue makes two Trident Strike attacks."),
     act("Trident Strike","<i>Melee Weapon Attack:</i> +8 to hit, reach 10 ft., one target. <i>Hit:</i> 16 (2d10 + 5) Piercing plus 7 (2d6) Psychic damage."),
     act("Unidentified Terror (Recharge 5-6)","Nue becomes incomprehensible in a 20-foot radius aura. DC 17 Wisdom save or 35 (10d6) Psychic damage, Frightened, and unable to distinguish friend from foe until end of next turn. On success, half.")],
    [rx("Chimeric Evasion","When Nue is targeted by an attack or spell, she alters her form, imposing disadvantage on the triggering roll.")],
    description="The Unidentified Mysterious Beast")

make_char("Yuuma Toutetsu","Team True Terror","Fiend (Gozu-Tenno)","chaotic evil","Large","Natural Armor",17,12,12,"40 ft.",
    {"strength":24,"dexterity":12,"constitution":22,"intelligence":12,"wisdom":10,"charisma":16},
    ["strength","constitution"],["Athletics","Intimidation","Perception"],
    [],["bludgeoning, piercing, and slashing from nonmagical attacks"],[],["Frightened","Charmed","Poisoned"],
    ["darkvision 60 ft."],["Common","Infernal"],
    [ab("All-Devouring Maw","Yuuma can swallow a Grappled Medium-or-smaller creature. It makes DC 18 Strength save or be swallowed: Blinded, Restrained, 21 (6d6) Acid damage per turn. If Yuuma takes 25+ damage in one turn from inside, she regurgitates within 10 feet."),
     ab("Voracious","Advantage on attack rolls against Grappled or Restrained creatures.")],
    [act("Multiattack","Yuuma makes one Bite and one Claw attack."),
     act("Bite","<i>Melee Weapon Attack:</i> +10 to hit, reach 5 ft., one target. <i>Hit:</i> 22 (2d12 + 9) Piercing plus 14 (4d6) Acid damage. Large or smaller: DC 18 Strength save or Grappled (escape DC 18)."),
     act("Claw","<i>Melee Weapon Attack:</i> +10 to hit, reach 10 ft., one target. <i>Hit:</i> 20 (2d10 + 9) Slashing damage."),
     act("Consuming Roar (Recharge 5-6)","A roar in a 30-foot radius. DC 18 Strength save or 42 (12d6) Force damage and pulled 10 feet toward Yuuma. On success, half.")],
    [rx("Snatch","When a creature within 10 feet misses Yuuma with melee, she attempts to Grapple it (contested Strength).")],
    description="The All-Devouring Taotie of Insatiable Hunger",environment="Underground")

make_char("Hata no Kokoro","Team True Terror","Construct (Menreiki)","neutral","Medium","Natural Armor",15,10,8,"35 ft.",
    {"strength":10,"dexterity":18,"constitution":14,"intelligence":14,"wisdom":16,"charisma":20},
    ["charisma","wisdom"],["Performance","Insight","Perception"],
    [],[],["poison"],["Poisoned","Charmed","Frightened"],["darkvision 60 ft."],["Common"],
    [ab("66 Masks","As a bonus action, Kokoro changes active mask: Rage Mask (allies +4 damage), Sorrow Mask (enemies within 30 ft. have disadvantage on attacks), or Joy Mask (allies immune to Frightened and Charmed)."),
     ab("Emotion Surge","Creatures within 30 feet feel overwhelming versions of the active mask's emotion. CR 2 or lower creatures may flee, submit, or act erratically.")],
    [act("Multiattack","Kokoro makes two Mask Slash attacks."),
     act("Mask Slash","<i>Melee Weapon Attack:</i> +7 to hit, reach 5 ft., one target. <i>Hit:</i> 16 (2d10 + 5) Slashing plus 7 (2d6) Psychic damage."),
     act("Emotional Pandemonium (Recharge 5-6)","Kokoro rapidly cycles masks in a 30-foot radius. DC 17 Wisdom save or 35 (10d6) Psychic damage and Confused until end of next turn. On success, half.")],
    [rx("Mask Switch","When Kokoro is targeted by attack or spell, she switches her active mask. The attacker makes DC 16 Wisdom save or the attack/spell misses.")],
    description="The Menreiki of Sixty-Six Masks and Emotions")

print("\nTeam Fortune Favors:")
make_char("Mike Goutokuji","Team Fortune Favors","Fey (Maneki Neko)","neutral good","Small","Natural Armor",14,10,8,"35 ft.",
    {"strength":10,"dexterity":18,"constitution":14,"intelligence":14,"wisdom":16,"charisma":20},
    ["charisma","wisdom"],["Persuasion","Insight","Perception"],[],[],[],["Charmed","Frightened"],
    ["darkvision 60 ft."],["Common","Sylvan"],
    [ab("Fortune's Favor","Mike and allies within 30 feet add +2 to all saving throws. Once per short rest, Mike grants one creature within 30 feet advantage on its next roll."),
     ab("Beckoning Paw","As a bonus action (range 60 ft.), Mike compels a creature: DC 16 Wisdom save or magically compelled to move its full speed toward Mike (provokes OA). Allies comply willingly.")],
    [act("Multiattack","Mike makes two Lucky Strike attacks."),
     act("Lucky Strike","<i>Melee Weapon Attack:</i> +7 to hit, reach 5 ft., one target. <i>Hit:</i> 14 (2d10 + 3) Force damage. On a critical hit: DC 16 Charisma save or Stunned until end of next turn."),
     act("Fortune Wave (Recharge 5-6)","Mike waves in a 30-foot radius. Allied creatures regain 21 (6d6) HP. Enemies: DC 17 Charisma save or 35 (10d6) Force damage. On success, half.")],
    [rx("Lucky Intercept","When an ally within 30 feet rolls a death saving throw, Mike grants +5 to the roll.")],
    description="The Maneki Neko Fairy of Fortune and Good Luck")

make_char("Tewi Inaba","Team Fortune Favors","Fey (Youkai Rabbit)","neutral","Small","Natural Armor",15,10,6,"40 ft.",
    {"strength":8,"dexterity":20,"constitution":14,"intelligence":16,"wisdom":14,"charisma":18},
    ["dexterity","charisma"],["Stealth","Deception","Persuasion","Acrobatics"],[],[],[],[],
    ["darkvision 60 ft."],["Common","Sylvan"],
    [ab("Earth Rabbit's Luck","As a bonus action, Tewi grants a luck token to one creature within 30 feet. The creature can expend it to reroll one roll. Up to 3 tokens distributed at once."),
     ab("Ancient Rabbit","Advantage on all saves against spells and magical effects. Cannot be magically aged.")],
    [act("Multiattack","Tewi makes three Rabbit Punch attacks."),
     act("Rabbit Punch","<i>Melee Weapon Attack:</i> +8 to hit, reach 5 ft., one target. <i>Hit:</i> 10 (2d4 + 5) Bludgeoning damage. DC 16 Dexterity save or knocked Prone."),
     act("Misfortune Trap (Recharge 5-6)","Misfortune in a 20-foot radius. DC 16 Charisma save or 35 (10d6) Force damage and disadvantage on all rolls until end of next turn. On success, half.")],
    [rx("Nimble Rabbit","When Tewi is targeted by an attack, she imposes disadvantage on the triggering roll.")],
    description="The Ancestral Earth Rabbit Who Brings Good Fortune",environment="Forest")

make_char("Eternity Larva","Team Fortune Favors","Fey (Butterfly Fairy)","chaotic good","Small","Natural Armor",14,10,8,"30 ft., Fly 50 ft.",
    {"strength":8,"dexterity":18,"constitution":14,"intelligence":12,"wisdom":12,"charisma":18},
    ["dexterity","charisma"],["Stealth","Perception","Acrobatics"],
    [],["poison"],["poison"],["Poisoned"],["darkvision 60 ft."],["Common","Sylvan"],
    [ab("Metamorphosis","When Eternity drops below half HP, she gains +4 AC, +20 ft. speed, and attacks deal +7 (2d6) Poison damage for the rest of the encounter."),
     ab("Fairy Dust","As a bonus action in a 10-foot radius: allied creatures have advantage on their next save; enemies: DC 15 Constitution save or Poisoned until end of next turn.")],
    [act("Multiattack","Eternity makes two Wing Blade attacks."),
     act("Wing Blade","<i>Melee Weapon Attack:</i> +7 to hit, reach 5 ft., one target. <i>Hit:</i> 11 (2d6 + 4) Slashing plus 7 (2d6) Poison damage."),
     act("Eternal Bloom (Recharge 5-6)","Life energy in a 20-foot radius. Allies regain 21 (6d6) HP. Enemies: DC 15 Constitution save or 28 (8d6) Poison damage and Poisoned for 1 minute. On success, half.")],
    [rx("Butterfly Wing Evasion","When Eternity is hit by a melee attack, she flutters up to 20 feet. If out of reach, the damage is halved.")],
    description="The Butterfly Fairy of Metamorphosis and Eternity",environment="Forest")

print("\nTeam Butteryfries:")
make_char("Yuyuko Saigyouji","Team Butteryfries","Undead (Ghost Princess)","neutral","Medium","Natural Armor",16,12,8,"35 ft., Fly 40 ft.",
    {"strength":10,"dexterity":16,"constitution":16,"intelligence":16,"wisdom":14,"charisma":22},
    ["charisma","wisdom"],["Perception","Insight","Deception"],
    [],["necrotic"],["poison"],["Poisoned","Charmed","Frightened","Exhaustion"],
    ["truesight 30 ft.", "darkvision 60 ft."],["Common","Elvish"],
    [ab("Death Invitation","Yuyuko invites death on a living creature within 60 feet below 50 HP. DC 18 Charisma save or die instantly. Undead, Constructs, and death ward immune. Once per long rest."),
     ab("Ghost's Incorporeality","Not in sunlight: Yuyuko can move through creatures and objects as difficult terrain. Takes 5 Force damage ending her turn inside an object.")],
    [act("Multiattack","Yuyuko makes two Ghostly Touch attacks."),
     act("Ghostly Touch","<i>Melee Spell Attack:</i> +9 to hit, reach 5 ft., one target. <i>Hit:</i> 21 (3d10 + 5) Necrotic damage. Target cannot regain HP until start of its next turn."),
     act("Saigyou Ayakashi (Recharge 5-6)","Yuyuko channels the cherry tree in a 30-foot radius. Each living creature: DC 18 Wisdom save or 35 (10d6) Necrotic damage and Incapacitated until end of next turn. On success, half.")],
    [rx("Death Redirect","When an allied creature within 30 feet drops to 0 HP, Yuyuko absorbs the killing blow herself, reducing absorbed damage by 14 (4d6).")],
    description="The Ghost Princess of the Netherworld's Hakugyokurou")

make_char("Youmu Konpaku","Team Butteryfries","Humanoid (Half-Ghost)","lawful good","Medium","Natural Armor",18,10,8,"40 ft.",
    {"strength":18,"dexterity":22,"constitution":16,"intelligence":14,"wisdom":16,"charisma":12},
    ["dexterity","strength"],["Athletics","Acrobatics","Perception","Stealth"],
    [],["necrotic"],[],[],["darkvision 60 ft."],["Common"],
    [ab("Two-Sword Style","When Youmu takes her Multiattack, she adds her proficiency bonus to one additional attack roll. If both swords hit the same target in one turn, it makes DC 16 Constitution save or be Stunned until end of next turn."),
     ab("Half-Ghost Presence","Youmu's ghost half occupies the same space as another creature. As a bonus action she grants an adjacent ally +3 AC until start of her next turn.")],
    [act("Multiattack","Youmu makes three Sword Strike attacks."),
     act("Sword Strike","<i>Melee Weapon Attack:</i> +9 to hit, reach 5 ft., one target. <i>Hit:</i> 17 (2d10 + 6) Slashing damage."),
     act("Slash of Evanescence (Recharge 5-6)","A perfect slash in a 30-foot line. DC 17 Dexterity save or 42 (12d6) Slashing damage and Blinded until end of next turn. On success, half.")],
    [rx("Perfect Guard","When Youmu is hit by a melee attack, she parries, reducing the damage by 17 (2d10 + 6).")],
    description="Half-Human, Half-Ghost Swordswoman of the Netherworld")

make_char("Komachi Onozuka","Team Butteryfries","Fey (Shinigami)","chaotic neutral","Medium","Natural Armor",16,12,8,"35 ft., Fly 40 ft.",
    {"strength":18,"dexterity":14,"constitution":16,"intelligence":12,"wisdom":14,"charisma":18},
    ["strength","charisma"],["Perception","Intimidation","Athletics","Insight"],
    [],["necrotic"],[],["Charmed","Frightened","Poisoned"],["truesight 30 ft.", "darkvision 60 ft."],["Common","Infernal"],
    [ab("Scythe of the River Styx","Komachi's scythe attacks are magical and ignore resistance to Necrotic damage. On a hit, she can push or pull the target up to 20 feet (no save)."),
     ab("Distance Manipulation","As a bonus action, Komachi teleports herself up to 30 feet closer to or farther from one target she can see.")],
    [act("Multiattack","Komachi makes two Scythe Strike attacks."),
     act("Scythe Strike","<i>Melee Weapon Attack:</i> +7 to hit, reach 10 ft., one target. <i>Hit:</i> 21 (3d10 + 5) Slashing plus 9 (2d8) Necrotic damage."),
     act("River of Death (Recharge 5-6)","Komachi sweeps in a 30-foot radius. DC 17 Constitution save or 35 (10d6) Necrotic damage and unable to regain HP until end of next turn. On success, half.")],
    [rx("Ferrywoman's Dodge","When Komachi would be hit by an attack, she teleports up to 30 feet. If out of range, the attack misses.")],
    description="The Leisurely Shinigami Ferryman of the Sanzu River")

print("\nTeam Hidden Star:")
make_char("Okina Matara","Team Hidden Star","Fey (Secret God)","neutral","Medium","Natural Armor",17,12,8,"35 ft.",
    {"strength":14,"dexterity":16,"constitution":18,"intelligence":20,"wisdom":18,"charisma":22},
    ["wisdom","charisma"],["Arcana","History","Perception","Insight"],
    [],["bludgeoning, piercing, and slashing from nonmagical attacks"],[],["Charmed","Frightened","Paralyzed"],
    ["truesight 60 ft."],["Common","Sylvan","Celestial"],
    [ab("Secret God's Backdoors","As a bonus action, Okina opens a backdoor in a solid surface within 60 feet (up to 3 simultaneously). Allies moving through a backdoor teleport to another backdoor she has created."),
     ab("Hidden Power","As a bonus action (once per long rest per creature), Okina grants a creature a Hidden Talent: proficiency in one skill of her choice and advantage on its next 3 rolls with that skill.")],
    [act("Multiattack","Okina makes two Matara Strike attacks."),
     act("Matara Strike","<i>Ranged Spell Attack:</i> +9 to hit, range 60 ft., one target. <i>Hit:</i> 22 (4d10) Force damage."),
     act("Secret God's Revelation (Recharge 5-6)","Okina reveals her true nature in a 30-foot radius. DC 19 Wisdom save or 35 (10d6) Psychic damage and Stunned until end of next turn. On success, half.")],
    [rx("Backdoor Escape","When Okina is targeted by an attack, she steps through a backdoor, teleporting up to 60 feet. The attack misses.")],
    description="The Secret God Behind the Curtains of All Creation")

make_char("Satono Nishida","Team Hidden Star","Fey (Shintai)","neutral","Medium","Natural Armor",14,10,8,"35 ft., Fly 40 ft.",
    {"strength":10,"dexterity":16,"constitution":14,"intelligence":14,"wisdom":16,"charisma":20},
    ["charisma","wisdom"],["Performance","Perception","Persuasion"],[],[],[],["Charmed","Frightened"],
    ["darkvision 60 ft."],["Common","Sylvan"],
    [ab("Dance of Emptying","When Satono dances (bonus action), creatures of her choice within 30 feet: DC 16 Wisdom save or one of the following drained for 1 minute: speed halved, attacks at disadvantage, or cannot use bonus actions."),
     ab("Spiritual Amplifier","Allied spellcasters within 30 feet add +2 to spell attack rolls and save DCs.")],
    [act("Multiattack","Satono makes two Dance Strike attacks."),
     act("Dance Strike","<i>Melee Weapon Attack:</i> +6 to hit, reach 5 ft., one target. <i>Hit:</i> 16 (2d10 + 5) Force damage. DC 16 Wisdom save or lose one active buff effect."),
     act("Emptying Dance (Recharge 5-6)","Satono dances in a 30-foot radius. DC 16 Wisdom save or 35 (10d6) Psychic damage, speed 0, and no reactions until end of next turn. On success, half.")],
    [rx("Graceful Whirl","When Satono is hit by melee, she reduces the damage by 11 (2d10) and moves up to 10 feet.")],
    description="The Dancing Shintai of Okina's Left Side")

make_char("Mai Teireida","Team Hidden Star","Fey (Shintai)","neutral","Medium","Natural Armor",14,10,8,"35 ft., Fly 40 ft.",
    {"strength":10,"dexterity":18,"constitution":14,"intelligence":16,"wisdom":16,"charisma":20},
    ["charisma","dexterity"],["Performance","Perception","Acrobatics"],
    [],["cold"],[],[],["darkvision 60 ft."],["Common","Sylvan"],
    [ab("Dance of Filling","When Mai dances (bonus action), creatures of her choice within 30 feet gain one: +2 AC, advantage on attack rolls, or +1d6 to all damage rolls. One effect per creature at a time."),
     ab("Ice Magic","Mai's ranged attacks deal Cold damage. She ignores difficult terrain from ice and snow.")],
    [act("Multiattack","Mai makes two Frost Blade attacks."),
     act("Frost Blade","<i>Ranged Spell Attack:</i> +8 to hit, range 60 ft., one target. <i>Hit:</i> 16 (2d10 + 5) Cold damage. Target's speed reduced by 10 ft. until end of its next turn."),
     act("Filling Dance (Recharge 5-6)","Mai dances in a 30-foot radius. Allies regain 21 (6d6) HP and have advantage on next attack. Enemies: DC 16 Dexterity save or 28 (8d6) Cold damage and Restrained in ice until end of next turn. On success, half.")],
    [rx("Ice Veil","When Mai is targeted by a ranged attack, she forms an ice shield, gaining +4 AC against that attack.")],
    description="The Dancing Shintai of Okina's Right Side")

make_char("Star Sapphire","Team Hidden Star","Fey (Fairy)","neutral","Small","Natural Armor",14,10,8,"30 ft., Fly 50 ft.",
    {"strength":8,"dexterity":18,"constitution":14,"intelligence":16,"wisdom":18,"charisma":14},
    ["wisdom","dexterity"],["Perception","Stealth","Investigation"],
    [],["radiant"],[],[],["truesight 30 ft.", "darkvision 60 ft."],["Common","Sylvan"],
    [ab("Fairy Detection","Star Sapphire detects all living and magical creatures within 120 feet regardless of invisibility or barriers. Cannot be surprised. As a free action, she reveals an invisible creature's location, removing its Invisible condition against creatures that hear her until its next turn."),
     ab("Revealing Light","As a bonus action, Star Sapphire illuminates a 20-foot radius within 60 feet. Invisible creatures are revealed and cannot benefit from invisibility in the area for 1 minute.")],
    [act("Multiattack","Star Sapphire makes two Starlight Bolt attacks."),
     act("Starlight Bolt","<i>Ranged Spell Attack:</i> +7 to hit, range 60 ft., one target. <i>Hit:</i> 17 (3d8 + 4) Radiant damage."),
     act("Revelation Burst (Recharge 5-6)","A burst of star light in a 30-foot radius. All invisible creatures are revealed. DC 16 Wisdom save or 35 (10d6) Radiant damage and unable to benefit from invisibility for 1 minute. On success, half.")],
    [rx("Early Warning","When an ally within 60 feet would be surprised, Star Sapphire calls out a warning: negate surprise and grant +4 AC against first attack this round.")],
    description="The Fairy Who Senses the Presence of All Living Things",environment="Forest")

print("\nTeam Mountain Beasts:")
make_char("Mayumi Joutouguu","Team Mountain Beasts","Construct (Haniwa)","lawful neutral","Medium","Natural Armor",17,10,10,"35 ft.",
    {"strength":20,"dexterity":14,"constitution":18,"intelligence":14,"wisdom":14,"charisma":12},
    ["strength","constitution"],["Athletics","Perception","History"],
    [],["bludgeoning, piercing, and slashing from nonmagical attacks"],["poison"],
    ["Poisoned","Charmed","Frightened","Exhaustion"],["darkvision 60 ft."],["Common"],
    [ab("Haniwa Warrior","Made of sacred clay. Extra damage dice from critical hits are ignored."),
     ab("Arrowhead Captain","Allied Constructs and Undead within 30 feet have advantage on attack rolls and saves against Frightened.")],
    [act("Multiattack","Mayumi makes two Clay Arrow attacks, or two Haniwa Spear attacks."),
     act("Clay Arrow","<i>Ranged Weapon Attack:</i> +8 to hit, range 60/120 ft., one target. <i>Hit:</i> 16 (2d10 + 5) Piercing. Target's speed reduced by 10 ft. until end of its next turn."),
     act("Haniwa Spear","<i>Melee Weapon Attack:</i> +8 to hit, reach 10 ft., one target. <i>Hit:</i> 18 (2d12 + 5) Piercing damage."),
     act("Sacred Volley (Recharge 5-6)","Sacred arrows in a 30-foot cone. DC 16 Dexterity save or 35 (10d6) Piercing damage and knocked Prone. On success, half.")],
    [rx("Clay Fortification","When Mayumi takes damage, she reduces it by 14 (4d6) as her clay hardens.")],
    description="The Haniwa Warrior Captain of the Divine Spirit Mausoleum")

