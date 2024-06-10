from pokemon.pokemon_class import Pokemon


def swords_dance(user: Pokemon): # +2 atk function
    user.stage_change("attack", 2)

def nasty_plot(user: Pokemon): # +2 spa function
    user.stage_change("special_attack", 2)
