import Pokemon_Entwicklen
import Pokemon_Klassen
import Angriff_Klassen

evolution = Pokemon_Entwicklen.Evolution()

bauz = Pokemon_Klassen.Bauz(attacken=[Angriff_Klassen.Rasierblatt(), Angriff_Klassen.Fliegen()], level=10, maxkp=73)

pokemon = bauz

if evolution.check_evolution(pokemon) != None:
    pokemon = evolution.evolution(pokemon)
    print(pokemon.__dict__)