import Pokemon_Entwicklen
import Pokemon_Klassen
import Angriff_Klassen

entwickeln = Pokemon_Entwicklen.Entwicklung()

bauz = Pokemon_Klassen.Bauz(attacken=[Angriff_Klassen.Rasierblatt(), Angriff_Klassen.Fliegen()], fp=5, level=10)

print(entwickeln.check_evolution(bauz))
