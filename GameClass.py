import Altar_Klasse as Altar
import Trainer_Klasse as Trainer
from Pokemon_Klassen import Pokemon, all_pokemon
import Pokemon_Entwickeln
from Balancer_Klasse import Balancer
from Angriff_Klassen import Attacken
from Battle_Klasse import Battle
import random


class GameClass:
    def  __init__(self, spieler: Trainer.Spieler, altar: Altar.Altar_For_Sacrifices):
        self.spieler = spieler
        self.altar = altar
        self.selected_pokemon: Pokemon = None    # for viewing pokemon stats
        self.evolution: Pokemon_Entwickeln.Evolution = Pokemon_Entwickeln.Evolution()

    def choose_enemy(self):
        enemys = ["Team Fregen Rüpel", "Nick Fregen"]
        self.enemy_text = random.choices(enemys, weights=[99, 1], k=1)[0]

    def create_BattleClass(self):
        balancer = Balancer(all_pokemon, self.spieler.pokemon_team, Attacken)
        balanced_enemy_team = balancer.make_balanced_enemy_team(len(self.spieler.pokemon_team))
        enemy = Trainer.Enemy(self.enemy_text, balanced_enemy_team, balanced_enemy_team[0], balanced_enemy_team)
        self.battle = Battle(self.spieler.pokemon_team[0], self.spieler.pokemon_team, None, enemy.active_pokemon, enemy.pokemon_team, self.altar)

