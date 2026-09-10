import Altar_Klasse as Altar
import Trainer_Klasse as Trainer
from Pokemon_Klassen import Pokemon
import Pokemon_Entwickeln


class GameClass:
    def  __init__(self, spieler: Trainer.Spieler, altar: Altar.Altar_For_Sacrifices):
        self.spieler = spieler
        self.altar = altar
        self.selected_pokemon: Pokemon = None    # for viewing pokemon stats
        self.evolution: Pokemon_Entwickeln.Evolution = Pokemon_Entwickeln.Evolution()

