from Pokemon_Klassen import *

class Evolution:
    def __init__(self):
        pass

    evolutions = [
        ["Bauz", 10, "Arboretoss"],
        ["Arboretoss", 20, "Silvarro"],
        ["Flamiau", 10, "Miezunder"],
        ["Miezunder", 20 , "Fuegro"],
        ["Robball", 10, "Marikeck"],
        ["Marikeck", 20, "Primarene"],
    ]

    def check_evolution(self, pokemon: Pokemon) -> str:
        for evolution in self.evolutions:
            if evolution[0] == pokemon.name and pokemon.level >= evolution[1]:
                return evolution[2]

    def evolution(self, pokemon: Pokemon) -> Pokemon:
        pokemon = self.adjust_stats(pokemon)
        pokemon.name = self.check_evolution(pokemon)
        return pokemon

    def adjust_stats(self, pokemon: Pokemon) -> Pokemon:
        evolution = self.check_evolution(pokemon)
        evolution_cls = globals()[evolution]
        evolution_instance = evolution_cls()

        std_pokemon = pokemon.__class__
        std_values = std_pokemon()

        pokemon.maxkp = getattr(evolution_instance, "maxkp") + (pokemon.maxkp - std_values.maxkp)
        pokemon.currentkp = pokemon.maxkp
        pokemon.atk = getattr(evolution_instance, "atk") + (pokemon.atk - std_values.atk)
        pokemon.defence = getattr(evolution_instance, "defence") + (pokemon.defence - std_values.defence)
        pokemon.spatk = getattr(evolution_instance, "spatk") + (pokemon.spatk - std_values.spatk)
        pokemon.spdef = getattr(evolution_instance, "spdef") + (pokemon.spdef - std_values.spdef)
        pokemon.init = getattr(evolution_instance, "init") + (pokemon.init - std_values.init)

        pokemon.typ = getattr(evolution_instance, "typ")

        pokemon.front_img = getattr(evolution_instance, "front_img")
        pokemon.back_img = getattr(evolution_instance, "back_img")
        return pokemon
