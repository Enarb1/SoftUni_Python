def draw_cards(*args, **kwargs):
    monsters = []
    spells = []

    for name, card_type in (list(args) + list(kwargs.items())):
        if card_type == 'monster':
            monsters.append(f"  ***{name}")
        elif card_type == 'spell':
            spells.append(f"  $$${name}")

    monsters = sorted(monsters, reverse=True)
    spells = sorted(spells)

    result = ""
    if monsters:
        result += "Monster cards:\n" + '\n'.join(monsters)
    if spells:
        result += "\nSpell cards:\n" + '\n'.join(spells)

    return result