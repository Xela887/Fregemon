import random
from Pokemon_Klassen import all_pokemon
from Angriff_Klassen import Attacken


class Altar_For_Sacrifices:
    def __init__(self, spieler, pokemon_bodies=0, trainer_bodies=0, fp_amount=0, sacrifice_count=0):
        self.spieler = spieler
        self.pokemon_bodies = pokemon_bodies
        self.trainer_bodies = trainer_bodies
        self.sacrifice_count = sacrifice_count
        self.sac_for_pokemon_cost = 3
        self.change_attack_cost = 5
        self.sac_for_fp_cost = 5
        self.sac_for_fp_amount = 3
        self.fp_amount = fp_amount

    def sacrifice_for_pokemon(self):
        if self.pokemon_bodies >= 3 and self.trainer_bodies >= 3:
            self.pokemon_bodies -= 3
            self.trainer_bodies -= 3
            new_pokemon = random.choice(filter_pokemon_by_level(self.spieler, all_pokemon))
            roll_new = False
            while True:
                for poke in self.spieler.pokemonliste:
                    if new_pokemon().name == poke.name:
                        roll_new = True
                if roll_new == False:
                    break
                if roll_new == True:
                    new_pokemon = random.choice(filter_pokemon_by_level(self.spieler, all_pokemon))
                    roll_new = False
            self.spieler.add_pokemon(new_pokemon(attacken=[zufalls_attacke(dmgtype="physisch", typ=getattr(new_pokemon(), "typ")[0]), zufalls_attacke(dmgtype="spezial", typ=getattr(new_pokemon(), "typ")[0])]))

    def sacrifice_for_zp(self):
        if self.pokemon_bodies >= self.sac_for_fp_cost:
            amount = self.pokemon_bodies // self.sac_for_fp_cost
            self.pokemon_bodies -= amount * self.sac_for_fp_cost
            self.fp_amount += amount * self.sac_for_fp_amount


def zufalls_attacke(typ = None, dmgtype = None):
    gefiltert = []
    for cls in Attacken:
        instanz = cls()
        if (typ is None or instanz.typ == typ) and (dmgtype is None or instanz.dmgtype == dmgtype):
            gefiltert.append(cls)

    if not gefiltert:
        raise ValueError(f"Keine Attacke gefunden mit Typ={typ} und dmgtype={dmgtype}")

    return random.choice(gefiltert)()

def filter_pokemon_by_level(spieler, all_pokemon):
    filtered_list = []
    for poke in all_pokemon:
        if poke().level <= get_average_stat(spieler, "level", "poketeam"):
            filtered_list.append(poke)
    return filtered_list

def get_average_stat(spieler, stat, place):
    count = 0
    average_stat = 0
    if place == "poketeam":
        place = spieler.pokemon_team
    elif place == "pokelist":
        place = spieler.pokemonliste
    for poke in place:
        count += 1
        average_stat += getattr(poke, stat)
    return average_stat // count