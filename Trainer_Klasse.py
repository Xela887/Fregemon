

class Trainer:
    def __init__(self, name, pokemonliste=None, active_pokemon=None, pokemon_team=[]):
        self.name = name
        self.active_pokemon = active_pokemon
        self.pokemon_team = pokemon_team
        if pokemonliste is None:
            self.pokemonliste = []
        else:
            self.pokemonliste = pokemonliste

    def add_pokemon(self, pokemon):
        self.pokemonliste.append(pokemon)
        return

class Spieler(Trainer):
    def __init__(self, name, pokemonliste, active_pokemon, pokemon_team):
        super().__init__(name, pokemonliste, active_pokemon, pokemon_team)

    def swap_pokemon(self, slot):
        self.active_pokemon = self.pokemon_team[slot]


class Enemy(Trainer):
    def __init__(self, name, pokemonliste, active_pokemon, pokemon_team):
        super().__init__(name, pokemonliste, active_pokemon, pokemon_team)