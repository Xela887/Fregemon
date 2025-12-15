import random

class Balancer:
    def __init__(self, all_pokemon, spieler_pokemon_team):
        self.all_pokemon = all_pokemon
        self.spieler_pokemon_team = spieler_pokemon_team
        self.balanced_enemy_team = []


    def make_balanced_enemy_team(self, amount_pokemon):
        for i in range(amount_pokemon):
            self.make_balanced_enemy_pokemon()
        return self.balanced_enemy_team

    def make_balanced_enemy_pokemon(self):
        pokemon = self.get_random_pokemon()
        pokemon.level = self.get_average_stat("level") + self.get_random_level_adder()
        pokemon.maxkp = self.get_average_stat("maxkp") + self.get_random_stat_adder()
        pokemon.atk = self.get_average_stat("atk") + self.get_random_stat_adder()
        pokemon.atk = self.get_average_stat("defence") + self.get_random_stat_adder()
        pokemon.atk = self.get_average_stat("spatk") + self.get_random_stat_adder()
        pokemon.atk = self.get_average_stat("spdef") + self.get_random_stat_adder()
        pokemon.atk = self.get_average_stat("init") + self.get_random_stat_adder()
        self.balanced_enemy_team.append(pokemon)

    def get_random_level_adder(self):
        level_adder = random.randint(-5, 5)
        return level_adder

    def get_random_stat_adder(self):
        stat_adder = random.randint(-20, 20)
        return stat_adder

    def get_average_stat(self, stat):
        count = 0
        average_stat = 0
        for poke in self.spieler_pokemon_team:
            count += 1
            average_stat += getattr(poke, stat)
        return average_stat // count

    def filter_pokemon_by_level(self):
        filtered_list = []
        for poke in self.all_pokemon:
            if poke().level <= self.get_average_stat("level"):
                filtered_list.append(poke)
        return filtered_list

    def get_random_pokemon(self):
        random_pokemon = random.choice(self.filter_pokemon_by_level())
        return random_pokemon
