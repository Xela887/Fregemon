import Angriff_Klassen


class pokemon:
    def __init__(self, name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp = None, fp=0):
        self.name = name
        self.maxkp = maxkp
        if currentkp is None:
            self.currentkp = maxkp
        else:
            self.currentkp = currentkp
        self.ep = 0
        self.level = level
        self.typ = typ
        self.atk = atk
        self.defence = defence
        self.spatk = spatk
        self.spdef = spdef
        self.init = init
        self.attacken = attacken
        self.fp = fp

#Individuelle Pokemon als Unterklasse von "Pokemon".
#Stats kommen von https://pokewiki.de/Liste_der_Pok%C3%A9mon_nach_Alola-Pok%C3%A9dex


class Bauz(pokemon):
    def __init__(self, name="Bauz", maxkp=68, typ=["Pflanze", "Flug"], atk=55, defence=55, spatk=50, spdef=50, level=1, init=42, currentkp=68, attacken=2, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, level, init, currentkp, attacken, fp)


class Arboretoss(pokemon):
    def __init__(self, name="Arboretoss", maxkp=78, typ=["Pflanze", "Flug"], atk=75, defence=75, spatk=70, spdef=70, level=10, init=52, currentkp=78, attacken=2, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, level, init, currentkp, attacken, fp)


class Silvarro(pokemon):
    def __init__(self, name="Silvarro", maxkp=78, typ=["Pflanze", "Geist"], atk=107, defence=75, spatk=100, spdef=100, level=30, init=70, currentkp=78, attacken=2, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, level, init, currentkp, attacken, fp)


class Flamiau(pokemon):
    def __init__(self, name="Flamiau", maxkp=45, typ=["Feuer"], atk=65, defence=40, spatk=60, spdef=40, level=1, init=70, currentkp=45, attacken=2, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, level, init, currentkp, attacken, fp)


class Miezunder(pokemon):
    def __init__(self, name="Miezunder", maxkp=65, typ=["Feuer"], atk=85, defence=50, spatk=80, spdef=50, level=10, init=90, currentkp=65, attacken=2, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, level, init, currentkp, attacken, fp)


class Fuegro(pokemon):
    def __init__(self, name="Fuegro", maxkp=95, typ=["Feuer", "Unlicht"], atk=115, defence=90, spatk=80, spdef=90, level=20, init=60, currentkp=95, attacken=2, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, level, init, currentkp, attacken, fp)


class Robball(pokemon):
    def __init__(self, name="Robball", maxkp=50, typ=["Wasser"], atk=50, defence=54, spatk=66, spdef=56, level=1, init=40, currentkp=50, attacken=2, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, level, init, currentkp, attacken, fp)


class Marikeck(pokemon):
    def __init__(self, name="Marikeck", maxkp=60, typ=["Wasser"], atk=69, defence=69, spatk=91, spdef=81, level=10, init=50, currentkp=60, attacken=2, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, level, init, currentkp, attacken, fp)


class Primarene(pokemon):
    def __init__(self, name="Primarene", maxkp=80, typ=["Wasser", "Fee"], atk=74, defence=74, spatk=126, spdef=116, init=60, attacken=2, level=20, currentkp=80, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Peppeck(pokemon):
    def __init__(self, name="Peppeck", maxkp=35, typ=["Normal", "Flug"], atk=75, defence=30, spatk=30, spdef=30, init=65, attacken=2, level=1, currentkp=35, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Trompeck(pokemon):
    def __init__(self, name="Trompeck", maxkp=55, typ=["Normal", "Flug"], atk=85, defence=50, spatk=40, spdef=50, init=75, attacken=2, level=10, currentkp=55, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Tukanon(pokemon):
    def __init__(self, name="Tukanon", maxkp=80, typ=["Normal", "Flug"], atk=120, defence=75, spatk=75, spdef=75, init=60, attacken=2, level=20, currentkp=80, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Mangunior(pokemon):
    def __init__(self, name="Mangunior", maxkp=48, typ=["Normal"], atk=70, defence=30, spatk=30, spdef=30, init=45, attacken=2, level=1, currentkp=48, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Manguspektor(pokemon):
    def __init__(self, name="Manguspektor", maxkp=88, typ=["Normal"], atk=110, defence=60, spatk=55, spdef=60, init=45, attacken=2, level=10, currentkp=88, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Rattfratz(pokemon):
    def __init__(self, name="Rattfratz", maxkp=30, typ=["Normal"], atk=56, defence=35, spatk=25, spdef=35, init=72, attacken=2, level=1, currentkp=30, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Rattikarl(pokemon):
    def __init__(self, name="Rattikarl", maxkp=55, typ=["Normal"], atk=81, defence=60, spatk=50, spdef=70, init=97, attacken=2, level=10, currentkp=55, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Raupy(pokemon):
    def __init__(self, name="Raupy", maxkp=45, typ=["Käfer"], atk=30, defence=35, spatk=20, spdef=20, init=45, attacken=2, level=1, currentkp=45, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Safcon(pokemon):
    def __init__(self, name="Safcon", maxkp=50, typ=["Käfer"], atk=20, defence=55, spatk=25, spdef=25, init=30, attacken=2, level=10, currentkp=50, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Smettbo(pokemon):
    def __init__(self, name="Smettbo", maxkp=60, typ=["Käfer","Flug"], atk=45, defence=50, spatk=90, spdef=80, init=70, attacken=2, level=20, currentkp=60, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Ledyba(pokemon):
    def __init__(self, name="Ledyba", maxkp=40, typ=["Käfer","Flug"], atk=30, defence=40, spatk=55, spdef=55, init=60, attacken=2, level=1, currentkp=40, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Ledian(pokemon):
    def __init__(self, name="Ledian", maxkp=55, typ=["Käfer","Flug"], atk=50, defence=60, spatk=75, spdef=85, init=90, attacken=2, level=10, currentkp=55, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Webarak(pokemon):
    def __init__(self, name="Webarak", maxkp=40, typ=["Käfer","Gift"], atk=45, defence=50, spatk=55, spdef=40, init=75, attacken=2, level=1, currentkp=40, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Ariados(pokemon):
    def __init__(self, name="Ariados", maxkp=70, typ=["Käfer","Gift"], atk=90, defence=70, spatk=80, spdef=60, init=90, attacken=2, level=10, currentkp=70, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Pichu(pokemon):
    def __init__(self, name="Pichu", maxkp=20, typ=["Elektro"], atk=40, defence=15, spatk=35, spdef=35, init=60, attacken=2, level=1, currentkp=20, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Pikachu(pokemon):
    def __init__(self, name="Pikachu", maxkp=35, typ=["Elektro"], atk=55, defence=30, spatk=50, spdef=40, init=90, attacken=2, level=10, currentkp=35, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Raichu(pokemon):
    def __init__(self, name="Raichu", maxkp=60, typ=["Elektro"], atk=90, defence=55, spatk=90, spdef=80, init=110, attacken=2, level=20, currentkp=60, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Mabula(pokemon):
    def __init__(self, name="Mabula", maxkp=47, typ=["Käfer"], atk=62, defence=45, spatk=55, spdef=45, init=46, attacken=2, level=1, currentkp=47, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Akkup(pokemon):
    def __init__(self, name="Akkup", maxkp=57, typ=["Käfer","Elektro"], atk=82, defence=95, spatk=55, spdef=75, init=36, attacken=2, level=10, currentkp=57, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Donarion(pokemon):
    def __init__(self, name="Donarion", maxkp=77, typ=["Käfer","Elektro"], atk=70, defence=90, spatk=145, spdef=75, init=43, attacken=2, level=20, currentkp=77, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Mobai(pokemon):
    def __init__(self, name="Mobai", maxkp=40, typ=["Kampf"], atk=62, defence=44, spatk=48, spdef=43, init=55, attacken=2, level=1, currentkp=40, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Mogelbaum(pokemon):
    def __init__(self, name="Mogelbaum", maxkp=60, typ=["Kampf"], atk=82, defence=74, spatk=78, spdef=73, init=65, attacken=2, level=10, currentkp=60, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Wonneira(pokemon):
    def __init__(self, name="Wonneira", maxkp=100, typ=["Normal"], atk=5, defence=5, spatk=15, spdef=65, init=30, attacken=2, level=1, currentkp=100, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Chaneira(pokemon):
    def __init__(self, name="Chaneira", maxkp=250, typ=["Normal"], atk=5, defence=5, spatk=35, spdef=105, init=50, attacken=2, level=10, currentkp=250, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Heiteira(pokemon):
    def __init__(self, name="Heiteira", maxkp=360, typ=["Normal"], atk=5, defence=5, spatk=45, spdef=125, init=60, attacken=2, level=20, currentkp=360, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Mampfaxo(pokemon):
    def __init__(self, name="Mampfaxo", maxkp=160, typ=["Normal"], atk=130, defence=80, spatk=65, spdef=85, init=50, attacken=2, level=1, currentkp=160, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Relaxa(pokemon):
    def __init__(self, name="Relaxa", maxkp=330, typ=["Normal"], atk=160, defence=110, spatk=95, spdef=115, init=30, attacken=2, level=10, currentkp=330, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Flegmon(pokemon):
    def __init__(self, name="Flegmon", maxkp=90, typ=["Wasser","Psycho"], atk=65, defence=65, spatk=40, spdef=40, init=15, attacken=2, level=1, currentkp=90, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Lahmus(pokemon):
    def __init__(self, name="Lahmus", maxkp=140, typ=["Wasser","Psycho"], atk=85, defence=85, spatk=70, spdef=70, init=30, attacken=2, level=10, currentkp=140, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Laschoking(pokemon):
    def __init__(self, name="Laschoking", maxkp=190, typ=["Wasser","Psycho"], atk=105, defence=105, spatk=90, spdef=90, init=40, attacken=2, level=20, currentkp=190, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Wingul(pokemon):
    def __init__(self, name="Wingul", maxkp=40, typ=["Wasser","Flug"], atk=30, defence=30, spatk=55, spdef=30, init=85, attacken=2, level=1, currentkp=40, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Pelipper(pokemon):
    def __init__(self, name="Pelipper", maxkp=60, typ=["Wasser","Flug"], atk=50, defence=100, spatk=95, spdef=70, init=65, attacken=2, level=10, currentkp=60, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Abra(pokemon):
    def __init__(self, name="Abra", maxkp=25, typ=["Psycho"], atk=20, defence=15, spatk=105, spdef=55, init=90, attacken=2, level=1, currentkp=25, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Kadabra(pokemon):
    def __init__(self, name="Kadabra", maxkp=40, typ=["Psycho"], atk=35, defence=30, spatk=120, spdef=70, init=105, attacken=2, level=10, currentkp=40, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Simsala(pokemon):
    def __init__(self, name="Simsala", maxkp=55, typ=["Psycho"], atk=50, defence=45, spatk=135, spdef=95, init=120, attacken=2, level=20, currentkp=55, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Mauzi(pokemon):
    def __init__(self, name="Mauzi", maxkp=40, typ=["Normal"], atk=45, defence=35, spatk=40, spdef=40, init=90, attacken=2, level=1, currentkp=40, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Snobilikat(pokemon):
    def __init__(self, name="Snobilikat", maxkp=65, typ=["Normal"], atk=70, defence=60, spatk=65, spdef=65, init=115, attacken=2, level=10, currentkp=65, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Magnetilo(pokemon):
    def __init__(self, name="Magnetilo", maxkp=25, typ=["Elektro","Stahl"], atk=35, defence=70, spatk=95, spdef=55, init=45, attacken=2, level=1, currentkp=25, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Magneton(pokemon):
    def __init__(self, name="Magneton", maxkp=50, typ=["Elektro","Stahl"], atk=60, defence=95, spatk=120, spdef=70, init=70, attacken=2, level=10, currentkp=50, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Magnezone(pokemon):
    def __init__(self, name="Magnezone", maxkp=70, typ=["Elektro","Stahl"], atk=70, defence=115, spatk=150, spdef=90, init=80, attacken=2, level=20, currentkp=70, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Sleima(pokemon):
    def __init__(self, name="Sleima", maxkp=40, typ=["Gift"], atk=65, defence=64, spatk=40, spdef=40, init=32, attacken=2, level=1, currentkp=40, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Sleimok(pokemon):
    def __init__(self, name="Sleimok", maxkp=65, typ=["Gift"], atk=90, defence=89, spatk=55, spdef=55, init=42, attacken=2, level=10, currentkp=65, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Fukano(pokemon):
    def __init__(self, name="Fukano", maxkp=45, typ=["Feuer"], atk=60, defence=40, spatk=50, spdef=50, init=65, attacken=2, level=1, currentkp=45, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Arkani(pokemon):
    def __init__(self, name="Arkani", maxkp=75, typ=["Feuer"], atk=100, defence=70, spatk=80, spdef=80, init=95, attacken=2, level=10, currentkp=75, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Traumato(pokemon):
    def __init__(self, name="Traumato", maxkp=60, typ=["Psycho"], atk=65, defence=60, spatk=90, spdef=75, init=55, attacken=2, level=1, currentkp=60, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Hypno(pokemon):
    def __init__(self, name="Hypno", maxkp=85, typ=["Psycho"], atk=90, defence=85, spatk=115, spdef=100, init=70, attacken=2, level=10, currentkp=85, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Makuhita(pokemon):
    def __init__(self, name="Makuhita", maxkp=72, typ=["Kampf"], atk=60, defence=30, spatk=20, spdef=30, init=25, attacken=2, level=1, currentkp=72, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Hariyama(pokemon):
    def __init__(self, name="Hariyama", maxkp=144, typ=["Kampf"], atk=120, defence=60, spatk=40, spdef=60, init=50, attacken=2, level=10, currentkp=144, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Farbeagle(pokemon):
    def __init__(self, name="Farbeagle", maxkp=59, typ=["Normal"], atk=85, defence=50, spatk=55, spdef=50, init=92, attacken=2, level=1, currentkp=59, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Krabbox(pokemon):
    def __init__(self, name="Krabbox", maxkp=47, typ=["Kampf"], atk=82, defence=57, spatk=42, spdef=47, init=63, attacken=2, level=1, currentkp=47, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Krawell(pokemon):
    def __init__(self, name="Krawell", maxkp=97, typ=["Kampf", "Eis"], atk=132, defence=77, spatk=62, spdef=67, init=43, attacken=2, level=10, currentkp=97, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Nebulak(pokemon):
    def __init__(self, name="Nebulak", maxkp=30, typ=["Geist","Gift"], atk=40, defence=35, spatk=50, spdef=70, init=80, attacken=2, level=1, currentkp=30, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Alpollo(pokemon):
    def __init__(self, name="Alpollo", maxkp=45, typ=["Geist","Gift"], atk=50, defence=45, spatk=65, spdef=85, init=95, attacken=2, level=10, currentkp=45, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Gengar(pokemon):
    def __init__(self, name="Gengar", maxkp=60, typ=["Geist","Gift"], atk=65, defence=60, spatk=130, spdef=75, init=110, attacken=2, level=20, currentkp=60, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Driftlon(pokemon):
    def __init__(self, name="Driftlon", maxkp=110, typ=["Geist","Flug"], atk=60, defence=30, spatk=80, spdef=50, init=110, attacken=2, level=1, currentkp=110, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Drifzepeli(pokemon):
    def __init__(self, name="Drifzepeli", maxkp=150, typ=["Geist","Flug"], atk=80, defence=44, spatk=90, spdef=54, init=100, attacken=2, level=10, currentkp=150, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Traunfugil(pokemon):
    def __init__(self, name="Traunfugil", maxkp=190, typ=["Geist"], atk=100, defence=60, spatk=100, spdef=70, init=80, attacken=2, level=20, currentkp=190, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Traunmagil(pokemon):
    def __init__(self, name="Traunmagil", maxkp=45, typ=["Geist"], atk=50, defence=45, spatk=115, spdef=55, init=95, attacken=2, level=1, currentkp=45, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Zubat(pokemon):
    def __init__(self, name="Zubat", maxkp=40, typ=["Gift","Flug"], atk=45, defence=35, spatk=30, spdef=40, init=55, attacken=2, level=1, currentkp=40, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Golbat(pokemon):
    def __init__(self, name="Golbat", maxkp=75, typ=["Gift","Flug"], atk=80, defence=70, spatk=65, spdef=75, init=90, attacken=2, level=10, currentkp=75, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Iksbat(pokemon):
    def __init__(self, name="Iksbat", maxkp=85, typ=["Gift","Flug"], atk=90, defence=80, spatk=75, spdef=85, init=100, attacken=2, level=20, currentkp=85, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)

class Digda(pokemon):
    def __init__(self, name="Digda", maxkp=10, typ=["Boden"], atk=55, defence=25, spatk=35, spdef=45, init=95, attacken=2, level=1, currentkp=10, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Digdri(pokemon):
    def __init__(self, name="Digdri", maxkp=35, typ=["Boden"], atk=100, defence=50, spatk=70, spdef=80, init=120, attacken=2, level=10, currentkp=35, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Habitak(pokemon):
    def __init__(self, name="Habitak", maxkp=40, typ=["Normal","Flug"], atk=60, defence=30, spatk=31, spdef=31, init=70, attacken=2, level=1, currentkp=40, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Ibitak(pokemon):
    def __init__(self, name="Ibitak", maxkp=65, typ=["Normal","Flug"], atk=90, defence=65, spatk=61, spdef=61, init=100, attacken=2, level=10, currentkp=65, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Geronimatz(pokemon):
    def __init__(self, name="Geronimatz", maxkp=85, typ=["Normal","Flug"], atk=130, defence=95, spatk=71, spdef=71, init=121, attacken=2, level=20, currentkp=85, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Washakwil(pokemon):
    def __init__(self, name="Washakwil", maxkp=60, typ=["Normal","Kampf"], atk=80, defence=50, spatk=40, spdef=50, init=65, attacken=2, level=1, currentkp=60, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Slallyk(pokemon):
    def __init__(self, name="Slallyk", maxkp=90, typ=["Unlicht","Flug"], atk=120, defence=70, spatk=60, spdef=70, init=85, attacken=2, level=10, currentkp=90, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Grypheldis(pokemon):
    def __init__(self, name="Grypheldis", maxkp=130, typ=["Unlicht","Flug"], atk=160, defence=90, spatk=80, spdef=90, init=105, attacken=2, level=20, currentkp=130, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Menki(pokemon):
    def __init__(self, name="Menki", maxkp=40, typ=["Kampf"], atk=80, defence=35, spatk=35, spdef=45, init=70, attacken=2, level=1, currentkp=40, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Rasaff(pokemon):
    def __init__(self, name="Rasaff", maxkp=70, typ=["Kampf"], atk=120, defence=65, spatk=65, spdef=75, init=100, attacken=2, level=10, currentkp=70, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Botogel(pokemon):
    def __init__(self, name="Botogel", maxkp=50, typ=["Eis","Flug"], atk=70, defence=50, spatk=50, spdef=50, init=65, attacken=2, level=1, currentkp=50, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Choreogel_Feuer(pokemon):
    def __init__(self, name="Choreogel (Feuer)", maxkp=80, typ=["Feuer","Flug"], atk=90, defence=70, spatk=100, spdef=60, init=85, attacken=2, level=10, currentkp=80, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Choreogel_Psycho(pokemon):
    def __init__(self, name="Choreogel (Psycho)", maxkp=80, typ=["Psycho","Flug"], atk=70, defence=80, spatk=120, spdef=60, init=85, attacken=2, level=10, currentkp=80, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Choreogel_Geist(pokemon):
    def __init__(self, name="Choreogel (Geist)", maxkp=80, typ=["Geist","Flug"], atk=80, defence=70, spatk=110, spdef=60, init=85, attacken=2, level=10, currentkp=80, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Choreogel_Elektro(pokemon):
    def __init__(self, name="Choreogel (Elektro)", maxkp=80, typ=["Elektro","Flug"], atk=75, defence=75, spatk=115, spdef=60, init=85, attacken=2, level=10, currentkp=80, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Wommel(pokemon):
    def __init__(self, name="Wommel", maxkp=40, typ=["Käfer","Fee"], atk=45, defence=40, spatk=55, spdef=40, init=84, attacken=2, level=1, currentkp=40, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Bandelby(pokemon):
    def __init__(self, name="Bandelby", maxkp=60, typ=["Käfer","Fee"], atk=55, defence=60, spatk=95, spdef=70, init=124, attacken=2, level=10, currentkp=60, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Lilminip(pokemon):
    def __init__(self, name="Lilminip", maxkp=45, typ=["Pflanze"], atk=30, defence=55, spatk=65, spdef=75, init=40, attacken=2, level=1, currentkp=45, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Dressella(pokemon):
    def __init__(self, name="Dressella", maxkp=70, typ=["Pflanze"], atk=60, defence=75, spatk=110, spdef=75, init=90, attacken=2, level=1, currentkp=70, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Waumboll(pokemon):
    def __init__(self, name="Waumboll", maxkp=40, typ=["Pflanze","Fee"], atk=27, defence=60, spatk=37, spdef=50, init=66, attacken=2, level=1, currentkp=40, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Elfun(pokemon):
    def __init__(self, name="Elfun", maxkp=60, typ=["Pflanze","Fee"], atk=67, defence=85, spatk=77, spdef=75, init=116, attacken=2, level=10, currentkp=60, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Enton(pokemon):
    def __init__(self, name="Enton", maxkp=50, typ=["Wasser"], atk=52, defence=48, spatk=65, spdef=50, init=55, attacken=2, level=1, currentkp=50, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Entoron(pokemon):
    def __init__(self, name="Entoron", maxkp=80, typ=["Wasser"], atk=82, defence=78, spatk=95, spdef=80, init=85, attacken=2, level=10, currentkp=80, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Karpador(pokemon):
    def __init__(self, name="Karpador", maxkp=20, typ=["Wasser"], atk=10, defence=55, spatk=15, spdef=20, init=80, attacken=2, level=1, currentkp=20, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Garados(pokemon):
    def __init__(self, name="Garados", maxkp=95, typ=["Wasser","Flug"], atk=125, defence=79, spatk=60, spdef=100, init=81, attacken=2, level=10, currentkp=95, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Schmerbe(pokemon):
    def __init__(self, name="Schmerbe", maxkp=50, typ=["Wasser","Boden"], atk=48, defence=43, spatk=46, spdef=41, init=60, attacken=2, level=1, currentkp=50, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Welsar(pokemon):
    def __init__(self, name="Welsar", maxkp=110, typ=["Wasser","Boden"], atk=78, defence=73, spatk=76, spdef=71, init=60, attacken=2, level=10, currentkp=110, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Machollo(pokemon):
    def __init__(self, name="Machollo", maxkp=70, typ=["Kampf"], atk=80, defence=50, spatk=35, spdef=35, init=35, attacken=2, level=1, currentkp=70, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Maschock(pokemon):
    def __init__(self, name="Maschock", maxkp=80, typ=["Kampf"], atk=100, defence=70, spatk=50, spdef=60, init=45, attacken=2, level=10, currentkp=80, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Machomei(pokemon):
    def __init__(self, name="Machomei", maxkp=90, typ=["Kampf"], atk=130, defence=80, spatk=65, spdef=85, init=55, attacken=2, level=20, currentkp=90, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Kiesling(pokemon):
    def __init__(self, name="Kiesling", maxkp=55, typ=["Gestein"], atk=75, defence=85, spatk=25, spdef=25, init=15, attacken=2, level=1, currentkp=55, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Sedimantur(pokemon):
    def __init__(self, name="Sedimantur", maxkp=70, typ=["Gestein"], atk=105, defence=105, spatk=50, spdef=40, init=20, attacken=2, level=10, currentkp=70, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Brockoloss(pokemon):
    def __init__(self, name="Brockoloss", maxkp=85, typ=["Gestein"], atk=135, defence=130, spatk=60, spdef=80, init=25, attacken=2, level=20, currentkp=85, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Rocara(pokemon):
    def __init__(self, name="Rocara", maxkp=50, typ=["Gestein","Fee"], atk=50, defence=150, spatk=50, spdef=150, init=50, attacken=2, level=1, currentkp=50, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Zobiris(pokemon):
    def __init__(self, name="Zobiris", maxkp=50, typ=["Unlicht","Geist"], atk=75, defence=75, spatk=65, spdef=65, init=50, attacken=2, level=1, currentkp=50, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Wuffels(pokemon):
    def __init__(self, name="Wuffels", maxkp=45, typ=["Gestein"], atk=65, defence=40, spatk=30, spdef=40, init=60, attacken=2, level=1, currentkp=45, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Wolwerock(pokemon):
    def __init__(self, name="Wolwerock", maxkp=70, typ=["Gestein"], atk=90, defence=115, spatk=60, spdef=60, init=65, attacken=2, level=1, currentkp=70, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Pandir(pokemon):
    def __init__(self, name="Pandir", maxkp=60, typ=["Normal"], atk=60, defence=60, spatk=60, spdef=60, init=60, attacken=2, level=1, currentkp=60, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Tentacha(pokemon):
    def __init__(self, name="Tentacha", maxkp=40, typ=["Wasser","Gift"], atk=40, defence=35, spatk=50, spdef=100, init=70, attacken=2, level=1, currentkp=40, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Tentoxa(pokemon):
    def __init__(self, name="Tentoxa", maxkp=80, typ=["Wasser","Gift"], atk=70, defence=65, spatk=80, spdef=120, init=100, attacken=2, level=10, currentkp=80, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Finneon(pokemon):
    def __init__(self, name="Finneon", maxkp=49, typ=["Wasser"], atk=49, defence=56, spatk=49, spdef=61, init=66, attacken=2, level=1, currentkp=49, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Lumineon(pokemon):
    def __init__(self, name="Lumineon", maxkp=69, typ=["Wasser"], atk=69, defence=76, spatk=69, spdef=86, init=91, attacken=2, level=10, currentkp=69, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Lusardin(pokemon):
    def __init__(self, name="Lusardin", maxkp=45, typ=["Wasser"], atk=20, defence=20, spatk=25, spdef=25, init=40, attacken=2, level=1, currentkp=45, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Schwarmform_Lusardin(pokemon):
    def __init__(self, name="Schwarmform Lusardin", maxkp=45, typ=["Wasser"], atk=140, defence=130, spatk=140, spdef=135, init=30, attacken=2, level=1, currentkp=45, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Liebiskus(pokemon):
    def __init__(self, name="Liebiskus", maxkp=43, typ=["Wasser"], atk=30, defence=55, spatk=40, spdef=65, init=97, attacken=2, level=1, currentkp=43, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Corasonn(pokemon):
    def __init__(self, name="Corasonn", maxkp=65, typ=["Wasser","Gestein"], atk=55, defence=95, spatk=65, spdef=95, init=35, attacken=2, level=1, currentkp=65, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Garstella(pokemon):
    def __init__(self, name="Garstella", maxkp=50, typ=["Gift","Wasser"], atk=53, defence=62, spatk=43, spdef=52, init=45, attacken=2, level=1, currentkp=50, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Aggrostella(pokemon):
    def __init__(self, name="Aggrostella", maxkp=50, typ=["Gift","Wasser"], atk=63, defence=152, spatk=53, spdef=142, init=35, attacken=2, level=10, currentkp=50, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Muschas(pokemon):
    def __init__(self, name="Muschas", maxkp=30, typ=["Wasser"], atk=65, defence=100, spatk=45, spdef=25, init=40, attacken=2, level=1, currentkp=30, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Austos(pokemon):
    def __init__(self, name="Austos", maxkp=50, typ=["Wasser","Eis"], atk=95, defence=180, spatk=85, spdef=45, init=70, attacken=2, level=10, currentkp=50, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Kindwurm(pokemon):
    def __init__(self, name="Kindwurm", maxkp=45, typ=["Drache"], atk=75, defence=60, spatk=40, spdef=30, init=50, attacken=2, level=1, currentkp=45, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Draschel(pokemon):
    def __init__(self, name="Draschel", maxkp=65, typ=["Drache"], atk=95, defence=100, spatk=60, spdef=50, init=50, attacken=2, level=10, currentkp=65, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Brutalanda(pokemon):
    def __init__(self, name="Brutalanda", maxkp=95, typ=["Drache","Flug"], atk=135, defence=80, spatk=110, spdef=80, init=100, attacken=2, level=20, currentkp=95, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Yorkleff(pokemon):
    def __init__(self, name="Yorkleff", maxkp=45, typ=["Normal"], atk=60, defence=45, spatk=25, spdef=45, init=55, attacken=2, level=1, currentkp=45, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Terribark(pokemon):
    def __init__(self, name="Terribark", maxkp=65, typ=["Normal"], atk=80, defence=65, spatk=35, spdef=65, init=60, attacken=2, level=10, currentkp=65, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Bissbark(pokemon):
    def __init__(self, name="Bissbark", maxkp=85, typ=["Normal"], atk=110, defence=90, spatk=45, spdef=90, init=80, attacken=2, level=20, currentkp=85, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Evoli(pokemon):
    def __init__(self, name="Evoli", maxkp=55, typ=["Normal"], atk=55, defence=50, spatk=45, spdef=65, init=55, attacken=2, level=1, currentkp=55, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Aquana(pokemon):
    def __init__(self, name="Aquana", maxkp=130, typ=["Wasser"], atk=65, defence=60, spatk=110, spdef=95, init=65, attacken=2, level=1, currentkp=130, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Blitza(pokemon):
    def __init__(self, name="Blitza", maxkp=65, typ=["Elektro"], atk=65, defence=60, spatk=110, spdef=95, init=130, attacken=2, level=1, currentkp=65, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Flamara(pokemon):
    def __init__(self, name="Flamara", maxkp=65, typ=["Feuer"], atk=130, defence=60, spatk=95, spdef=110, init=65, attacken=2, level=1, currentkp=65, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Psiana(pokemon):
    def __init__(self, name="Psiana", maxkp=65, typ=["Psycho"], atk=65, defence=60, spatk=130, spdef=95, init=110, attacken=2, level=1, currentkp=65, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Nachtara(pokemon):
    def __init__(self, name="Nachtara", maxkp=95, typ=["Unlicht"], atk=65, defence=110, spatk=60, spdef=130, init=65, attacken=2, level=1, currentkp=95, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Folipurba(pokemon):
    def __init__(self, name="Folipurba", maxkp=65, typ=["Pflanze"], atk=110, defence=130, spatk=60, spdef=65, init=95, attacken=2, level=1, currentkp=65, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Glaziola(pokemon):
    def __init__(self, name="Glaziola", maxkp=65, typ=["Eis"], atk=60, defence=110, spatk=130, spdef=95, init=65, attacken=2, level=1, currentkp=65, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Feelinara(pokemon):
    def __init__(self, name="Feelinara", maxkp=95, typ=["Fee"], atk=65, defence=65, spatk=110, spdef=130, init=60, attacken=2, level=1, currentkp=95, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Pampuli(pokemon):
    def __init__(self, name="Pampuli", maxkp=70, typ=["Boden"], atk=100, defence=70, spatk=45, spdef=70, init=45, attacken=2, level=1, currentkp=70, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Pampross(pokemon):
    def __init__(self, name="Pampross", maxkp=100, typ=["Boden"], atk=125, defence=100, spatk=55, spdef=85, init=35, attacken=2, level=10, currentkp=100, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Fluffeluff(pokemon):
    def __init__(self, name="Fluffeluff", maxkp=90, typ=["Normal","Fee"], atk=30, defence=15, spatk=40, spdef=20, init=15, attacken=2, level=1, currentkp=90, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Pummeluff(pokemon):
    def __init__(self, name="Pummeluff", maxkp=115, typ=["Normal","Fee"], atk=45, defence=20, spatk=45, spdef=25, init=20, attacken=2, level=10, currentkp=115, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Knuddeluff(pokemon):
    def __init__(self, name="Knuddeluff", maxkp=140, typ=["Normal","Fee"], atk=70, defence=45, spatk=85, spdef=50, init=45, attacken=2, level=20, currentkp=140, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Tauros(pokemon):
    def __init__(self, name="Tauros", maxkp=75, typ=["Normal"], atk=100, defence=95, spatk=40, spdef=70, init=110, attacken=2, level=1, currentkp=75, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Miltank(pokemon):
    def __init__(self, name="Miltank", maxkp=95, typ=["Normal"], atk=80, defence=105, spatk=40, spdef=70, init=100, attacken=2, level=1, currentkp=95, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Gehweiher(pokemon):
    def __init__(self, name="Gehweiher", maxkp=40, typ=["Käfer","Wasser"], atk=30, defence=32, spatk=50, spdef=52, init=65, attacken=2, level=1, currentkp=40, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Maskeregen(pokemon):
    def __init__(self, name="Maskeregen", maxkp=70, typ=["Käfer","Flug"], atk=60, defence=62, spatk=100, spdef=82, init=80, attacken=2, level=10, currentkp=70, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Araqua(pokemon):
    def __init__(self, name="Araqua", maxkp=38, typ=["Wasser","Käfer"], atk=40, defence=52, spatk=40, spdef=72, init=27, attacken=2, level=1, currentkp=38, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Aranestro(pokemon):
    def __init__(self, name="Aranestro", maxkp=68, typ=["Wasser","Käfer"], atk=70, defence=92, spatk=50, spdef=132, init=42, attacken=2, level=10, currentkp=68, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Imantis(pokemon):
    def __init__(self, name="Imantis", maxkp=40, typ=["Pflanze"], atk=55, defence=35, spatk=50, spdef=35, init=35, attacken=2, level=1, currentkp=40, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Mantidea(pokemon):
    def __init__(self, name="Mantidea", maxkp=70, typ=["Pflanze"], atk=105, defence=90, spatk=80, spdef=90, init=45, attacken=2, level=1, currentkp=70, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Bubungus(pokemon):
    def __init__(self, name="Bubungus", maxkp=50, typ=["Pflanze","Fee"], atk=35, defence=55, spatk=65, spdef=75, init=15, attacken=2, level=1, currentkp=50, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Lamellux(pokemon):
    def __init__(self, name="Lamellux", maxkp=60, typ=["Pflanze","Fee"], atk=75, defence=80, spatk=90, spdef=100, init=30, attacken=2, level=10, currentkp=60, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Paras(pokemon):
    def __init__(self, name="Paras", maxkp=35, typ=["Käfer","Pflanze"], atk=70, defence=55, spatk=45, spdef=55, init=25, attacken=2, level=1, currentkp=35, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Parasek(pokemon):
    def __init__(self, name="Parasek", maxkp=60, typ=["Käfer","Pflanze"], atk=95, defence=80, spatk=60, spdef=80, init=30, attacken=2, level=10, currentkp=60, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Quapsel(pokemon):
    def __init__(self, name="Quapsel", maxkp=44, typ=["Wasser","Kampf"], atk=50, defence=43, spatk=40, spdef=40, init=65, attacken=2, level=1, currentkp=44, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Quaputzi(pokemon):
    def __init__(self, name="Quaputzi", maxkp=65, typ=["Wasser","Kampf"], atk=65, defence=65, spatk=50, spdef=50, init=90, attacken=2, level=10, currentkp=65, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Quappo(pokemon):
    def __init__(self, name="Quappo", maxkp=90, typ=["Wasser","Kampf"], atk=95, defence=95, spatk=70, spdef=90, init=70, attacken=2, level=20, currentkp=90, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Quaxo(pokemon):
    def __init__(self, name="Quaxo", maxkp=90, typ=["Wasser"], atk=75, defence=75, spatk=90, spdef=100, init=70, attacken=2, level=20, currentkp=90, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Goldini(pokemon):
    def __init__(self, name="Goldini", maxkp=45, typ=["Wasser"], atk=67, defence=60, spatk=35, spdef=50, init=63, attacken=2, level=1, currentkp=45, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Golking(pokemon):
    def __init__(self, name="Golking", maxkp=80, typ=["Wasser"], atk=92, defence=65, spatk=65, spdef=80, init=68, attacken=2, level=1, currentkp=80, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Barschwa(pokemon):
    def __init__(self, name="Barschwa", maxkp=20, typ=["Wasser"], atk=15, defence=20, spatk=10, spdef=55, init=80, attacken=2, level=1, currentkp=20, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Milotic(pokemon):
    def __init__(self, name="Milotic", maxkp=95, typ=["Wasser"], atk=60, defence=79, spatk=100, spdef=125, init=81, attacken=2, level=10, currentkp=95, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Mamolida(pokemon):
    def __init__(self, name="Mamolida", maxkp=165, typ=["Wasser"], atk=75, defence=80, spatk=40, spdef=45, init=65, attacken=2, level=1, currentkp=165, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Dartiri(pokemon):
    def __init__(self, name="Dartiri", maxkp=45, typ=["Normal","Flug"], atk=50, defence=43, spatk=40, spdef=38, init=62, attacken=2, level=1, currentkp=39, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Dartignis(pokemon):
    def __init__(self, name="Dartignis", maxkp=62, typ=["Feuer","Flug"], atk=73, defence=55, spatk=56, spdef=52, init=84, attacken=2, level=10, currentkp=62, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Fiaro(pokemon):
    def __init__(self, name="Fiaro", maxkp=78, typ=["Feuer","Flug"], atk=84, defence=78, spatk=109, spdef=85, init=100, attacken=2, level=20, currentkp=78, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Molunk(pokemon):
    def __init__(self, name="Molunk", maxkp=48, typ=["Gift","Feuer"], atk=44, defence=40, spatk=71, spdef=40, init=77, attacken=2, level=1, currentkp=48, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Amfira(pokemon):
    def __init__(self, name="Amfira", maxkp=68, typ=["Gift","Feuer"], atk=64, defence=60, spatk=111, spdef=60, init=117, attacken=2, level=10, currentkp=68, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Tragosso(pokemon):
    def __init__(self, name="Tragosso", maxkp=50, typ=["Feuer"], atk=50, defence=95, spatk=40, spdef=50, init=35, attacken=2, level=1, currentkp=50, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Knogga(pokemon):
    def __init__(self, name="Knogga", maxkp=60, typ=["Feuer","Geist"], atk=80, defence=110, spatk=50, spdef=80, init=45, attacken=2, level=10, currentkp=60, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Kangama(pokemon):
    def __init__(self, name="Kangama", maxkp=105, typ=["Normal"], atk=95, defence=80, spatk=40, spdef=80, init=90, attacken=2, level=1, currentkp=105, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Magby(pokemon):
    def __init__(self, name="Magby", maxkp=45, typ=["Feuer"], atk=75, defence=37, spatk=70, spdef=55, init=83, attacken=2, level=1, currentkp=45, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Magmar(pokemon):
    def __init__(self, name="Magmar", maxkp=65, typ=["Feuer"], atk=95, defence=57, spatk=100, spdef=85, init=93, attacken=2, level=10, currentkp=65, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Magbrand(pokemon):
    def __init__(self, name="Magbrand", maxkp=75, typ=["Feuer"], atk=95, defence=67, spatk=125, spdef=95, init=83, attacken=2, level=20, currentkp=75, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Velursi(pokemon):
    def __init__(self, name="Velursi", maxkp=70, typ=["Normal","Kampf"], atk=75, defence=50, spatk=45, spdef=50, init=50, attacken=2, level=1, currentkp=70, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Kosturso(pokemon):
    def __init__(self, name="Kosturso", maxkp=120, typ=["Normal","Kampf"], atk=125, defence=80, spatk=55, spdef=60, init=60, attacken=2, level=10, currentkp=120, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Frubberl(pokemon):
    def __init__(self, name="Frubberl", maxkp=42, typ=["Pflanze"], atk=30, defence=38, spatk=30, spdef=38, init=32, attacken=2, level=1, currentkp=42, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Frubaila(pokemon):
    def __init__(self, name="Frubaila", maxkp=52, typ=["Pflanze"], atk=40, defence=48, spatk=40, spdef=48, init=62, attacken=2, level=10, currentkp=52, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Fruyal(pokemon):
    def __init__(self, name="Fruyal", maxkp=72, typ=["Pflanze"], atk=120, defence=98, spatk=50, spdef=98, init=72, attacken=2, level=20, currentkp=72, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Curelei(pokemon):
    def __init__(self, name="Curelei", maxkp=51, typ=["Fee"], atk=52, defence=90, spatk=82, spdef=110, init=100, attacken=2, level=1, currentkp=51, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Pinsir(pokemon):
    def __init__(self, name="Pinsir", maxkp=65, typ=["Käfer"], atk=125, defence=100, spatk=55, spdef=70, init=85, attacken=2, level=1, currentkp=65, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Kommandutan(pokemon):
    def __init__(self, name="Kommandutan", maxkp=90, typ=["Normal","Psycho"], atk=60, defence=80, spatk=90, spdef=110, init=60, attacken=2, level=1, currentkp=60, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Quartermak(pokemon):
    def __init__(self, name="Quartermak", maxkp=100, typ=["Kampf"], atk=120, defence=90, spatk=40, spdef=60, init=80, attacken=2, level=1, currentkp=100, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Viscora(pokemon):
    def __init__(self, name="Viscora", maxkp=45, typ=["Drache"], atk=50, defence=35, spatk=55, spdef=75, init=40, attacken=2, level=1, currentkp=45, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Viscargot(pokemon):
    def __init__(self, name="Viscargot", maxkp=68, typ=["Drache"], atk=75, defence=53, spatk=83, spdef=113, init=60, attacken=2, level=10, currentkp=68, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Viscogon(pokemon):
    def __init__(self, name="Viscogon", maxkp=90, typ=["Drache"], atk=100, defence=70, spatk=110, spdef=150, init=80, attacken=2, level=20, currentkp=90, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Formeo(pokemon):
    def __init__(self, name="Formeo", maxkp=70, typ=["Normal"], atk=70, defence=70, spatk=70, spdef=70, init=70, attacken=2, level=1, currentkp=70, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Reißlaus(pokemon):
    def __init__(self, name="Reißlaus", maxkp=25, typ=["Käfer","Wasser"], atk=25, defence=40, spatk=20, spdef=30, init=80, attacken=2, level=1, currentkp=25, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Tectass(pokemon):
    def __init__(self, name="Tectass", maxkp=75, typ=["Käfer","Wasser"], atk=125, defence=140, spatk=60, spdef=90, init=40, attacken=2, level=10, currentkp=75, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Sterndu(pokemon):
    def __init__(self, name="Sterndu", maxkp=30, typ=["Wasser","Psycho"], atk=45, defence=55, spatk=70, spdef=55, init=85, attacken=2, level=1, currentkp=30, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Starmie(pokemon):
    def __init__(self, name="Starmie", maxkp=60, typ=["Wasser","Psycho"], atk=75, defence=85, spatk=100, spdef=85, init=115, attacken=2, level=10, currentkp=60, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Sankabuh(pokemon):
    def __init__(self, name="Sankabuh", maxkp=55, typ=["Geist","Boden"], atk=55, defence=80, spatk=70, spdef=45, init=15, attacken=2, level=1, currentkp=55, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Colossand(pokemon):
    def __init__(self, name="Colossand", maxkp=85, typ=["Geist","Boden"], atk=75, defence=110, spatk=100, spdef=75, init=35, attacken=2, level=10, currentkp=85, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Koknodon(pokemon):
    def __init__(self, name="Koknodon", maxkp=67, typ=["Gestein"], atk=125, defence=40, spatk=30, spdef=30, init=58, attacken=2, level=1, currentkp=67, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Rameidon(pokemon):
    def __init__(self, name="Rameidon", maxkp=97, typ=["Gestein"], atk=165, defence=60, spatk=65, spdef=50, init=58, attacken=2, level=10, currentkp=97, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Schilterus(pokemon):
    def __init__(self, name="Schilterus", maxkp=30, typ=["Gestein","Stahl"], atk=42, defence=118, spatk=42, spdef=88, init=30, attacken=2, level=1, currentkp=30, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Bollterus(pokemon):
    def __init__(self, name="Bollterus", maxkp=60, typ=["Gestein","Stahl"], atk=52, defence=168, spatk=47, spdef=138, init=30, attacken=2, level=10, currentkp=60, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Flapteryx(pokemon):
    def __init__(self, name="Flapteryx", maxkp=55, typ=["Gestein","Flug"], atk=112, defence=45, spatk=74, spdef=45, init=70, attacken=2, level=1, currentkp=55, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Aeropteryx(pokemon):
    def __init__(self, name="Aeropteryx", maxkp=75, typ=["Gestein","Flug"], atk=140, defence=65, spatk=112, spdef=65, init=110, attacken=2, level=10, currentkp=75, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Galapaflos(pokemon):
    def __init__(self, name="Galapaflos", maxkp=54, typ=["Wasser","Gestein"], atk=78, defence=103, spatk=53, spdef=45, init=22, attacken=2, level=1, currentkp=54, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Karippas(pokemon):
    def __init__(self, name="Karippas", maxkp=74, typ=["Wasser","Gestein"], atk=108, defence=133, spatk=83, spdef=65, init=32, attacken=2, level=1, currentkp=74, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Paragoni(pokemon):
    def __init__(self, name="Paragoni", maxkp=43, typ=["Geist","Pflanze"], atk=70, defence=48, spatk=50, spdef=60, init=38, attacken=2, level=1, currentkp=43, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Trombork(pokemon):
    def __init__(self, name="Trombork", maxkp=85, typ=["Geist","Pflanze"], atk=110, defence=76, spatk=65, spdef=82, init=56, attacken=2, level=10, currentkp=85, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Nasgnet(pokemon):
    def __init__(self, name="Nasgnet", maxkp=30, typ=["Gestein"], atk=45, defence=135, spatk=45, spdef=90, init=30, attacken=2, level=1, currentkp=30, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Voluminas(pokemon):
    def __init__(self, name="Voluminas", maxkp=60, typ=["Gestein","Stahl"], atk=55, defence=145, spatk=75, spdef=150, init=40, attacken=2, level=10, currentkp=60, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Gufa(pokemon):
    def __init__(self, name="Gufa", maxkp=55, typ=["Wasser"], atk=60, defence=130, spatk=30, spdef=130, init=5, attacken=2, level=1, currentkp=55, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Lampi(pokemon):
    def __init__(self, name="Lampi", maxkp=75, typ=["Wasser","Elektro"], atk=38, defence=38, spatk=56, spdef=56, init=67, attacken=2, level=1, currentkp=75, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Lanturn(pokemon):
    def __init__(self, name="Lanturn", maxkp=125, typ=["Wasser","Elektro"], atk=58, defence=58, spatk=76, spdef=76, init=67, attacken=2, level=10, currentkp=125, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Typ_Null(pokemon):
    def __init__(self, name="Typ:Null", maxkp=95, typ=["Normal"], atk=95, defence=95, spatk=95, spdef=95, init=59, attacken=2, level=1, currentkp=95, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Amigento(pokemon):
    def __init__(self, name="Amigento", maxkp=95, typ=["Normal"], atk=95, defence=95, spatk=95, spdef=95, init=95, attacken=2, level=1, currentkp=95, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Unratütox(pokemon):
    def __init__(self, name="Unratütox", maxkp=50, typ=["Gift"], atk=50, defence=62, spatk=40, spdef=62, init=65, attacken=2, level=1, currentkp=50, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Deponitox(pokemon):
    def __init__(self, name="Deponitox", maxkp=80, typ=["Gift"], atk=95, defence=82, spatk=60, spdef=82, init=75, attacken=2, level=10, currentkp=80, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Panzaeron(pokemon):
    def __init__(self, name="Panzaeron", maxkp=65, typ=["Stahl","Flug"], atk=80, defence=140, spatk=40, spdef=70, init=70, attacken=2, level=1, currentkp=65, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Ditto(pokemon):
    def __init__(self, name="Ditto", maxkp=48, typ=["Normal"], atk=48, defence=48, spatk=48, spdef=48, init=48, attacken=2, level=1, currentkp=48, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Pii(pokemon):
    def __init__(self, name="Pii", maxkp=50, typ=["Fee"], atk=25, defence=28, spatk=45, spdef=55, init=15, attacken=2, level=1, currentkp=50, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Piepi(pokemon):
    def __init__(self, name="Piepi", maxkp=70, typ=["Fee"], atk=45, defence=48, spatk=60, spdef=65, init=35, attacken=2, level=10, currentkp=70, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Pixi(pokemon):
    def __init__(self, name="Pixi", maxkp=95, typ=["Fee"], atk=70, defence=73, spatk=95, spdef=90, init=60, attacken=2, level=20, currentkp=95, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Meteno(pokemon):
    def __init__(self, name="Meteno", maxkp=60, typ=["Gestein","Flug"], atk=60, defence=100, spatk=60, spdef=100, init=60, attacken=2, level=1, currentkp=60, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Tanhel(pokemon):
    def init__(self, name="Tanhel", maxkp=40, typ=["Stahl","Psycho"], atk=55, defence=80, spatk=35, spdef=60, init=30, attacken=2, level=1, currentkp=50, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Metang(pokemon):
    def __init__(self, name="Metang", maxkp=60, typ=["Stahl","Psycho"], atk=75, defence=100, spatk=55, spdef=80, init=50, attacken=2, level=10, currentkp=60, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Metagross(pokemon):
    def __init__(self, name="Metagross", maxkp=80, typ=["Stahl","Psycho"], atk=135, defence=130, spatk=95, spdef=90, init=70, attacken=2, level=20, currentkp=80, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Porygon(pokemon):
    def __init__(self, name="Porygon", maxkp=65, typ=["Normal"], atk=60, defence=70, spatk=85, spdef=75, init=40, attacken=2, level=1, currentkp=65, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Porygon2(pokemon):
    def __init__(self, name="Porygon2", maxkp=85, typ=["Normal"], atk=80, defence=90, spatk=105, spdef=95, init=60, attacken=2, level=10, currentkp=85, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Porygon_Z(pokemon):
    def __init__(self, name="Porygon-Z", maxkp=85, typ=["Normal"], atk=80, defence=70, spatk=135, spdef=75, init=90, attacken=2, level=20, currentkp=85, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Pam_Pam(pokemon):
    def __init__(self, name="Pam-Pam", maxkp=67, typ=["Kampf"], atk=82, defence=62, spatk=46, spdef=48, init=43, attacken=2, level=1, currentkp=67, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Pandagro(pokemon):
    def __init__(self, name="Pandagro", maxkp=95, typ=["Kampf","Unlicht"], atk=124, defence=78, spatk=69, spdef=71, init=58, attacken=2, level=10, currentkp=95, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Koalelu(pokemon):
    def __init__(self, name="Koalelu", maxkp=65, typ=["Normal"], atk=115, defence=65, spatk=75, spdef=95, init=65, attacken=2, level=1, currentkp=65, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Qurtel(pokemon):
    def __init__(self, name="Qurtel", maxkp=70, typ=["Feuer"], atk=85, defence=140, spatk=85, spdef=70, init=20, attacken=2, level=1, currentkp=70, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Tortunator(pokemon):
    def __init__(self, name="Tortunator", maxkp=60, typ=["Feuer","Drache"], atk=78, defence=135, spatk=91, spdef=85, init=36, attacken=2, level=1, currentkp=60, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Togedemaru(pokemon):
    def __init__(self, name="Togedemaru", maxkp=65, typ=["Elektro","Stahl"], atk=98, defence=63, spatk=40, spdef=73, init=96, attacken=2, level=1, currentkp=65, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Elekid(pokemon):
    def __init__(self, name="Elekid", maxkp=45, typ=["Elektro"], atk=63, defence=37, spatk=65, spdef=55, init=95, attacken=2, level=1, currentkp=45, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Elektek(pokemon):
    def __init__(self, name="Elektek", maxkp=65, typ=["Elektro"], atk=83, defence=57, spatk=95, spdef=85, init=105, attacken=2, level=10, currentkp=65, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Elevoltek(pokemon):
    def __init__(self, name="Elevoltek", maxkp=75, typ=["Elektro"], atk=123, defence=67, spatk=95, spdef=85, init=95, attacken=2, level=20, currentkp=75, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Kleinstein(pokemon):
    def __init__(self, name="Kleinstein", maxkp=40, typ=["Gestein","Elektro"], atk=80, defence=100, spatk=30, spdef=30, init=20, attacken=2, level=1, currentkp=40, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Georok(pokemon):
    def __init__(self, name="Georok", maxkp=55, typ=["Gestein","Elektro"], atk=95, defence=115, spatk=45, spdef=45, init=35, attacken=2, level=10, currentkp=55, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Geowaz(pokemon):
    def __init__(self, name="Geowaz", maxkp=80, typ=["Gestein","Elektro"], atk=120, defence=130, spatk=55, spdef=65, init=45, attacken=2, level=20, currentkp=80, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Ganovil(pokemon):
    def __init__(self, name="Ganovil", maxkp=50, typ=["Boden","Unlicht"], atk=72, defence=35, spatk=35, spdef=35, init=65, attacken=2, level=1, currentkp=50, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Rokkaiman(pokemon):
    def __init__(self, name="Rokkaiman", maxkp=60, typ=["Boden","Unlicht"], atk=82, defence=45, spatk=45, spdef=45, init=74, attacken=2, level=10, currentkp=60, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Rabigator(pokemon):
    def __init__(self, name="Rabigator", maxkp=95, typ=["Boden","Unlicht"], atk=117, defence=80, spatk=65, spdef=70, init=92, attacken=2, level=20, currentkp=95, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Knacklion(pokemon):
    def __init__(self, name="Knacklion", maxkp=45, typ=["Boden"], atk=100, defence=45, spatk=45, spdef=45, init=10, attacken=2, level=1, currentkp=50, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Vibrava(pokemon):
    def __init__(self, name="Vibrava", maxkp=50, typ=["Boden","Drache"], atk=70, defence=50, spatk=50, spdef=50, init=70, attacken=2, level=10, currentkp=50, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Libelldra(pokemon):
    def __init__(self, name="Libelldra", maxkp=80, typ=["Boden","Drache"], atk=100, defence=80, spatk=80, spdef=80, init=100, attacken=2, level=20, currentkp=80, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Kaumalat(pokemon):
    def __init__(self, name="Kaumalat", maxkp=58, typ=["Drache","Boden"], atk=70, defence=45, spatk=40, spdef=45, init=42, attacken=2, level=1, currentkp=58, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Knarksel(pokemon):
    def __init__(self, name="Knarksel", maxkp=68, typ=["Drache","Boden"], atk=90, defence=65, spatk=50, spdef=55, init=82, attacken=2, level=10, currentkp=68, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Knakrack(pokemon):
    def __init__(self, name="Knakrack", maxkp=108, typ=["Drache","Boden"], atk=130, defence=95, spatk=80, spdef=85, init=102, attacken=2, level=20, currentkp=108, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Clavion(pokemon):
    def __init__(self, name="Clavion", maxkp=57, typ=["Stahl","Fee"], atk=80, defence=91, spatk=80, spdef=87, init=75, attacken=2, level=1, currentkp=57, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Mimigma(pokemon):
    def __init__(self, name="Mimigma", maxkp=55, typ=["Geist","Fee"], atk=90, defence=80, spatk=50, spdef=105, init=96, attacken=2, level=1, currentkp=55, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Knirfish(pokemon):
    def __init__(self, name="Knirfish", maxkp=68, typ=["Wasser","Psycho"], atk=105, defence=70, spatk=70, spdef=70, init=92, attacken=2, level=1, currentkp=50, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Sen_Long(pokemon):
    def __init__(self, name="Sen Long", maxkp=78, typ=["Normal","Drache"], atk=60, defence=85, spatk=135, spdef=91, init=36, attacken=2, level=1, currentkp=100, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Absol(pokemon):
    def __init__(self, name="Absol", maxkp=65, typ=["Unlicht"], atk=130, defence=60, spatk=75, spdef=60, init=75, attacken=2, level=1, currentkp=65, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Schneppke(pokemon):
    def __init__(self, name="Schneppke", maxkp=50, typ=["Eis"], atk=50, defence=50, spatk=50, spdef=50, init=50, attacken=2, level=1, currentkp=50, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Firnontor(pokemon):
    def __init__(self, name="Firnontor", maxkp=80, typ=["Eis"], atk=80, defence=80, spatk=80, spdef=80, init=80, attacken=2, level=10, currentkp=80, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Frosdedje(pokemon):
    def __init__(self, name="Frosdedje", maxkp=70, typ=["Eis","Geist"], atk=80, defence=70, spatk=80, spdef=70, init=110, attacken=2, level=10, currentkp=72, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Sniebel(pokemon):
    def __init__(self, name="Sniebel", maxkp=55, typ=["Unlicht","Eis"], atk=95, defence=55, spatk=35, spdef=75, init=115, attacken=2, level=1, currentkp=55, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Snibunna(pokemon):
    def __init__(self, name="Snibunna", maxkp=70, typ=["Unlicht","Eis"], atk=120, defence=65, spatk=45, spdef=85, init=125, attacken=2, level=10, currentkp=60, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Sandan(pokemon):
    def __init__(self, name="Sandan", maxkp=50, typ=["Eis","Stahl"], atk=75, defence=90, spatk=10, spdef=35, init=40, attacken=2, level=1, currentkp=50, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Sandamer(pokemon):
    def __init__(self, name="Sandamer", maxkp=75, typ=["Eis","Stahl"], atk=100, defence=120, spatk=25, spdef=65, init=65, attacken=2, level=10, currentkp=75, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Vulpix(pokemon):
    def __init__(self, name="Vulpix", maxkp=38, typ=["Eis"], atk=41, defence=40, spatk=50, spdef=65, init=65, attacken=2, level=1, currentkp=38, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Vulnona(pokemon):
    def __init__(self, name="Vulnona", maxkp=73, typ=["Eis","Fee"], atk=76, defence=75, spatk=81, spdef=100, init=109, attacken=2, level=10, currentkp=73, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Gelatini(pokemon):
    def __init__(self, name="Gelatini", maxkp=36, typ=["Eis"], atk=50, defence=50, spatk=65, spdef=60, init=44, attacken=2, level=1, currentkp=36, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Gelatroppo(pokemon):
    def __init__(self, name="Gelatroppo", maxkp=51, typ=["Eis"], atk=65, defence=65, spatk=80, spdef=75, init=59, attacken=2, level=10, currentkp=51, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Gelatwino(pokemon):
    def __init__(self, name="Gelatwino", maxkp=71, typ=["Eis"], atk=95, defence=85, spatk=110, spdef=95, init=79, attacken=2, level=20, currentkp=71, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Snubbull(pokemon):
    def __init__(self, name="Snubbull", maxkp=60, typ=["Fee"], atk=80, defence=50, spatk=40, spdef=40, init=30, attacken=2, level=1, currentkp=60, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Granbull(pokemon):
    def __init__(self, name="Granbull", maxkp=90, typ=["Fee"], atk=120, defence=75, spatk=60, spdef=60, init=45, attacken=2, level=10, currentkp=90, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Schalellos(pokemon):
    def __init__(self, name="Schalellos", maxkp=76, typ=["Wasser"], atk=48, defence=48, spatk=57, spdef=62, init=34, attacken=2, level=1, currentkp=76, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Gastrodon(pokemon):
    def __init__(self, name="Gastrodon", maxkp=111, typ=["Wasser","Boden"], atk=83, defence=68, spatk=92, spdef=82, init=39, attacken=2, level=10, currentkp=111, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Relicanth(pokemon):
    def __init__(self, name="Relicanth", maxkp=100, typ=["Wasser","Gestein"], atk=90, defence=130, spatk=45, spdef=65, init=55, attacken=2, level=1, currentkp=100, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Moruda(pokemon):
    def __init__(self, name="Moruda", maxkp=70, typ=["Wasser","Unlicht"], atk=131, defence=100, spatk=86, spdef=90, init=40, attacken=2, level=1, currentkp=70, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Kanivanha(pokemon):
    def __init__(self, name="Kanivanha", maxkp=45, typ=["Wasser","Unlicht"], atk=90, defence=20, spatk=65, spdef=20, init=65, attacken=2, level=1, currentkp=50, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Tohaido(pokemon):
    def __init__(self, name="Tohaido", maxkp=70, typ=["Wasser","Unlicht"], atk=120, defence=40, spatk=95, spdef=40, init=95, attacken=2, level=10, currentkp=70, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Wailmer(pokemon):
    def __init__(self, name="Wailmer", maxkp=130, typ=["Wasser"], atk=70, defence=35, spatk=70, spdef=35, init=60, attacken=2, level=1, currentkp=130, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Wailord(pokemon):
    def __init__(self, name="Wailord", maxkp=170, typ=["Wasser"], atk=90, defence=45, spatk=90, spdef=45, init=60, attacken=2, level=20, currentkp=170, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Lapras(pokemon):
    def __init__(self, name="Lapras", maxkp=130, typ=["Wasser","Eis"], atk=85, defence=80, spatk=85, spdef=95, init=60, attacken=2, level=1, currentkp=130, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Owei(pokemon):
    def __init__(self, name="Owei", maxkp=60, typ=["Pflanze","Psycho"], atk=40, defence=80, spatk=60, spdef=45, init=40, attacken=2, level=1, currentkp=55, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Kokowei(pokemon):
    def __init__(self, name="Kokowei", maxkp=95, typ=["Pflanze","Psycho"], atk=105, defence=75, spatk=125, spdef=85, init=45, attacken=2, level=10, currentkp=95, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Miniras(pokemon):
    def __init__(self, name="Miniras", maxkp=45, typ=["Drache"], atk=55, defence=65, spatk=45, spdef=45, init=45, attacken=2, level=1, currentkp=45, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Mediras(pokemon):
    def __init__(self, name="Mediras", maxkp=55, typ=["Drache","Kampf"], atk=75, defence=90, spatk=65, spdef=70, init=65, attacken=2, level=10, currentkp=55, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Grandiras(pokemon):
    def __init__(self, name="Grandiras", maxkp=75, typ=["Drache","Kampf"], atk=110, defence=125, spatk=100, spdef=105, init=85, attacken=2, level=20, currentkp=75, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Emolga(pokemon):
    def __init__(self, name="Emolga", maxkp=55, typ=["Elektro","Flug"], atk=75, defence=60, spatk=75, spdef=60, init=103, attacken=2, level=1, currentkp=55, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Sichlor(pokemon):
    def __init__(self, name="Sichlor", maxkp=70, typ=["Käfer","Flug"], atk=110, defence=80, spatk=55, spdef=80, init=105, attacken=2, level=10, currentkp=70, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Scherox(pokemon):
    def __init__(self, name="Scherox", maxkp=70, typ=["Käfer","Stahl"], atk=130, defence=100, spatk=55, spdef=80, init=65, attacken=2, level=20, currentkp=70, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Kramurx(pokemon):
    def __init__(self, name="Kramurx", maxkp=60, typ=["Unlicht","Flug"], atk=85, defence=42, spatk=85, spdef=42, init=91, attacken=2, level=1, currentkp=60, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Kramshef(pokemon):
    def __init__(self, name="Kramshef", maxkp=100, typ=["Unlicht","Flug"], atk=125, defence=52, spatk=105, spdef=52, init=71, attacken=2, level=10, currentkp=100, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Riolu(pokemon):
    def __init__(self, name="Riolu", maxkp=40, typ=["Kampf"], atk=70, defence=40, spatk=35, spdef=40, init=60, attacken=2, level=1, currentkp=40, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Lucario(pokemon):
    def __init__(self, name="Lucario", maxkp=70, typ=["Kampf","Stahl"], atk=110, defence=70, spatk=115, spdef=70, init=90, attacken=2, level=10, currentkp=70, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Dratini(pokemon):
    def __init__(self, name="Dratini", maxkp=41, typ=["Drache"], atk=64, defence=45, spatk=50, spdef=50, init=50, attacken=2, level=1, currentkp=41, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Dragonir(pokemon):
    def __init__(self, name="Dragonir", maxkp=61, typ=["Drache"], atk=84, defence=65, spatk=70, spdef=70, init=70, attacken=2, level=10, currentkp=61, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Dragoran(pokemon):
    def __init__(self, name="Dragoran", maxkp=91, typ=["Drache","Flug"], atk=134, defence=95, spatk=100, spdef=100, init=80, attacken=2, level=20, currentkp=91, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Aerodactyl(pokemon):
    def __init__(self, name="Aerodactyl", maxkp=80, typ=["Gestein","Flug"], atk=105, defence=65, spatk=60, spdef=75, init=130, attacken=2, level=1, currentkp=80, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Kapu_Riki(pokemon):
    def __init__(self, name="Kapu-Riki", maxkp=70, typ=["Elektro","Fee"], atk=115, defence=85, spatk=95, spdef=75, init=130, attacken=2, level=1, currentkp=70, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Kapu_Fala(pokemon):
    def __init__(self, name="Kapu-Fala", maxkp=70, typ=["Psycho","Fee"], atk=85, defence=75, spatk=130, spdef=115, init=95, attacken=2, level=1, currentkp=70, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Kapu_Toro(pokemon):
    def __init__(self, name="Kapu-Toro", maxkp=70, typ=["Pflanze","Fee"], atk=130, defence=115, spatk=85, spdef=95, init=75, attacken=2, level=1, currentkp=70, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Kapu_Kime(pokemon):
    def __init__(self, name="Kapu-Kime", maxkp=70, typ=["Wasser","Fee"], atk=75, defence=115, spatk=95, spdef=130, init=85, attacken=2, level=1, currentkp=70, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Cosmog(pokemon):
    def __init__(self, name="Cosmog", maxkp=43, typ=["Psycho"], atk=29, defence=31, spatk=29, spdef=31, init=37, attacken=2, level=1, currentkp=43, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Cosmovum(pokemon):
    def __init__(self, name="Cosmovum", maxkp=43, typ=["Psycho"], atk=29, defence=131, spatk=29, spdef=131, init=37, attacken=2, level=1, currentkp=43, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Solgaleo(pokemon):
    def __init__(self, name="Solgaleo", maxkp=137, typ=["Psycho","Stahl"], atk=137, defence=107, spatk=113, spdef=89, init=97, attacken=2, level=1, currentkp=137, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Lunala(pokemon):
    def __init__(self, name="Lunala", maxkp=137, typ=["Psycho","Geist"], atk=113, defence=89, spatk=137, spdef=107, init=97, attacken=2, level=1, currentkp=137, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Anego(pokemon):
    def __init__(self, name="Anego", maxkp=109, typ=["Gestein","Gift"], atk=53, defence=47, spatk=127, spdef=131, init=103, attacken=2, level=1, currentkp=109, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Masskito(pokemon):
    def __init__(self, name="Masskito", maxkp=107, typ=["Käfer","Kampf "], atk=139, defence=139, spatk=53, spdef=53, init=79, attacken=2, level=1, currentkp=107, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Schabelle(pokemon):
    def __init__(self, name="Schabelle", maxkp=71, typ=["Käfer","Kampf"], atk=137, defence=37, spatk=137, spdef=37, init=151, attacken=2, level=1, currentkp=71, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Voltriant(pokemon):
    def __init__(self, name="Voltriant", maxkp=83, typ=["Elektro"], atk=89, defence=71, spatk=173, spdef=71, init=83, attacken=2, level=1, currentkp=83, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Kaguron(pokemon):
    def __init__(self, name="Kaguron", maxkp=97, typ=["Stahl","Flug"], atk=101, defence=103, spatk=107, spdef=101, init=61, attacken=2, level=1, currentkp=97, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Katagami(pokemon):
    def __init__(self, name="Katagami", maxkp=59, typ=["Stahl","Pflanze"], atk=181, defence=131, spatk=59, spdef=31, init=109, attacken=2, level=1, currentkp=59, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Schlingking(pokemon):
    def __init__(self, name="Schlingking", maxkp=223, typ=["Unlicht","Drache"], atk=101, defence=53, spatk=97, spdef=53, init=43, attacken=2, level=1, currentkp=223, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Necrozma(pokemon):
    def __init__(self, name="Necrozma", maxkp=97, typ=["Psycho"], atk=107, defence=101, spatk=127, spdef=89, init=79, attacken=2, level=1, currentkp=97, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Magearna(pokemon):
    def __init__(self, name="Magearna", maxkp=80, typ=["Stahl","Fee"], atk=95, defence=115, spatk=130, spdef=115, init=65, attacken=2, level=1, currentkp=80, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


class Marshadow(pokemon):
    def __init__(self, name="Marshadow", maxkp=90, typ=["Kampf","Geist"], atk=125, defence=80, spatk=90, spdef=90, init=125, attacken=2, level=1, currentkp=90, fp=0):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp)


        sacrifice_button = draw_button("Opfern", window_width * 0.40, window_height * 0.60, window_width * 0.20, window_height * 0.06)
        back_button = draw_button("Zurück", window_width * 0.40, window_height * 0.70, window_width * 0.20, window_height * 0.06)
        # Kein richtiger Knopf, nur Text in einem Feld
        available_bodys_text_field = draw_button("", window_width * 0.35, window_height * 0.40, window_width * 0.30, window_height * 0.15)

        available_trainer_bodys_text =draw_text("Besiegte Trainer: 0", windo
