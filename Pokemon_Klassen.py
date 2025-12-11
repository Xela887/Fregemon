# Pokemon
class Pokemon:
    def __init__(self, name, maxkp, typ, atk, defence, spatk, spdef, init, attacken=None, level=1, currentkp=None, fp=0, front_img=None, back_img=None):

        if attacken is None:
            attacken = []

        self.name = name
        self.maxkp = maxkp
        self.typ = typ
        self.atk = atk
        self.defence = defence
        self.spatk = spatk
        self.spdef = spdef
        self.init = init
        self.level = level
        self.ep = 0
        self.fp = fp
        self.front_img = front_img
        self.back_img = back_img

        if currentkp is None:
            self.currentkp = maxkp
        else:
            self.currentkp = currentkp

        self.attacken = attacken

        # Mindestwerte speichern
        self.base_maxkp = maxkp
        self.base_atk = atk
        self.base_def = defence
        self.base_spatk = spatk
        self.base_spdef = spdef
        self.base_init = init

    def check_level_up(self):
        if 100 * self.level ** 1.1 <= self.ep:
            self.ep = self.ep - 100 * self.level ** 1.1
            self.level += 1
            self.fp += 3

#Individuelle Pokemon als Unterklasse von "Pokemon".
class Bauz(Pokemon):
    def __init__(self, name="Bauz", maxkp=68, typ=["Pflanze", "Flug"], atk=55, defence=55, spatk=50, spdef=50, level=1, init=42, currentkp=68, attacken=[], fp=0, front_img="front_bauz_img", back_img="back_bauz_img"):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Arboretoss(Pokemon):
    def __init__(self, name="Arboretoss", maxkp=78, typ=["Pflanze", "Flug"], atk=75, defence=75, spatk=70, spdef=70, level=10, init=52, currentkp=78, attacken=[], fp=0, front_img="front_arboretoss_img", back_img="back_arboretoss_img"):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Silvarro(Pokemon):
    def __init__(self, name="Silvarro", maxkp=78, typ=["Pflanze", "Geist"], atk=107, defence=75, spatk=100, spdef=100, level=30, init=70, currentkp=78, attacken=[], fp=0, front_img="front_silvarro_img", back_img="back_silvarro_img"):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Flamiau(Pokemon):
    def __init__(self, name="Flamiau", maxkp=45, typ=["Feuer"], atk=65, defence=40, spatk=60, spdef=40, level=1, init=70, currentkp=45, attacken=[], fp=0, front_img="front_flamiau_img", back_img="back_flamiau_img"):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Miezunder(Pokemon):
    def __init__(self, name="Miezunder", maxkp=65, typ=["Feuer"], atk=85, defence=50, spatk=80, spdef=50, level=10, init=90, currentkp=65, attacken=[], fp=0, front_img="front_miezunder_img", back_img="back_miezunder_img"):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Fuegro(Pokemon):
    def __init__(self, name="Fuegro", maxkp=95, typ=["Feuer", "Unlicht"], atk=115, defence=90, spatk=80, spdef=90, level=20, init=60, currentkp=95, attacken=[], fp=0, front_img="front_fuegro_img", back_img="back_fuegro_img"):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Robball(Pokemon):
    def __init__(self, name="Robball", maxkp=50, typ=["Wasser"], atk=50, defence=54, spatk=66, spdef=56, level=1, init=40, currentkp=50, attacken=[], fp=0, front_img="front_robball_img", back_img="back_robball_img"):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Marikeck(Pokemon):
    def __init__(self, name="Marikeck", maxkp=60, typ=["Wasser"], atk=69, defence=69, spatk=91, spdef=81, level=10, init=50, currentkp=60, attacken=[], fp=0, front_img="front_marikeck_img", back_img="back_marikeck_img"):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Primarene(Pokemon):
    def __init__(self, name="Primarene", maxkp=80, typ=["Wasser", "Fee"], atk=74, defence=74, spatk=126, spdef=116, init=60, attacken=[], level=20, currentkp=80, fp=0, front_img="front_primarene_img", back_img="back_primarene_img"):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Peppeck(Pokemon):
    def __init__(self, name="Peppeck", maxkp=35, typ=["Normal", "Flug"], atk=75, defence=30, spatk=30, spdef=30, init=65, attacken=[], level=1, currentkp=35, fp=0, front_img="front_peppeck_img", back_img="back_peppeck_img"):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Trompeck(Pokemon):
    def __init__(self, name="Trompeck", maxkp=55, typ=["Normal", "Flug"], atk=85, defence=50, spatk=40, spdef=50, init=75, attacken=[], level=10, currentkp=55, fp=0, front_img="front_trompeck_img", back_img="back_trompeck_img"):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Tukanon(Pokemon):
    def __init__(self, name="Tukanon", maxkp=80, typ=["Normal", "Flug"], atk=120, defence=75, spatk=75, spdef=75, init=60, attacken=[], level=20, currentkp=80, fp=0, front_img="front_tukanon_img", back_img="back_tukanon_img"):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Mangunior(Pokemon):
    def __init__(self, name="Mangunior", maxkp=48, typ=["Normal"], atk=70, defence=30, spatk=30, spdef=30, init=45, attacken=[], level=1, currentkp=48, fp=0, front_img="front_mangunior_img", back_img="back_mangunior_img"):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Manguspektor(Pokemon):
    def __init__(self, name="Manguspektor", maxkp=88, typ=["Normal"], atk=110, defence=60, spatk=55, spdef=60, init=45, attacken=[], level=10, currentkp=88, fp=0, front_img="front_manguspektor_img", back_img="back_manguspektor_img"):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Mabula(Pokemon):
    def __init__(self, name="Mabula", maxkp=47, typ=["Käfer"], atk=62, defence=45, spatk=55, spdef=45, init=46, attacken=[], level=1, currentkp=47, fp=0, front_img="front_mabula_img", back_img="back_mabula_img"):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Akkup(Pokemon):
    def __init__(self, name="Akkup", maxkp=57, typ=["Käfer","Elektro"], atk=82, defence=95, spatk=55, spdef=75, init=36, attacken=[], level=10, currentkp=57, fp=0, front_img="front_akkup_img", back_img="back_akupp_img"):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Donarion(Pokemon):
    def __init__(self, name="Donarion", maxkp=77, typ=["Käfer","Elektro"], atk=70, defence=90, spatk=145, spdef=75, init=43, attacken=[], level=20, currentkp=77, fp=0, front_img="front_donarion_img", back_img="back_donarion_img"):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Krabbox(Pokemon):
    def __init__(self, name="Krabbox", maxkp=47, typ=["Kampf"], atk=82, defence=57, spatk=42, spdef=47, init=63, attacken=[], level=1, currentkp=47, fp=0, front_img="front_krabbox_img", back_img="back_krabbox_img"):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Krawell(Pokemon):
    def __init__(self, name="Krawell", maxkp=97, typ=["Kampf", "Eis"], atk=132, defence=77, spatk=62, spdef=67, init=43, attacken=[], level=10, currentkp=97, fp=0, front_img="front_krawell_img", back_img="back_krawell_img"):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Wommel(Pokemon):
    def __init__(self, name="Wommel", maxkp=40, typ=["Käfer","Fee"], atk=45, defence=40, spatk=55, spdef=40, init=84, attacken=[], level=1, currentkp=40, fp=0, front_img="front_wommel_img", back_img="back_wommel_img"):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Bandelby(Pokemon):
    def __init__(self, name="Bandelby", maxkp=60, typ=["Käfer","Fee"], atk=55, defence=60, spatk=95, spdef=70, init=124, attacken=[], level=10, currentkp=60, fp=0, front_img="front_bandelby_img", back_img="back_bandelby_img"):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Garstella(Pokemon):
    def __init__(self, name="Garstella", maxkp=50, typ=["Gift","Wasser"], atk=53, defence=62, spatk=43, spdef=52, init=45, attacken=[], level=1, currentkp=50, fp=0, front_img=None, back_img=None):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Aggrostella(Pokemon):
    def __init__(self, name="Aggrostella", maxkp=50, typ=["Gift","Wasser"], atk=63, defence=152, spatk=53, spdef=142, init=35, attacken=[], level=10, currentkp=50, fp=0, front_img=None, back_img=None):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Pampuli(Pokemon):
    def __init__(self, name="Pampuli", maxkp=70, typ=["Boden"], atk=100, defence=70, spatk=45, spdef=70, init=45, attacken=[], level=1, currentkp=70, fp=0, front_img=None, back_img=None):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Pampross(Pokemon):
    def __init__(self, name="Pampross", maxkp=100, typ=["Boden"], atk=125, defence=100, spatk=55, spdef=85, init=35, attacken=[], level=10, currentkp=100, fp=0, front_img=None, back_img=None):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Araqua(Pokemon):
    def __init__(self, name="Araqua", maxkp=38, typ=["Wasser","Käfer"], atk=40, defence=52, spatk=40, spdef=72, init=27, attacken=[], level=1, currentkp=38, fp=0, front_img=None, back_img=None):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Aranestro(Pokemon):
    def __init__(self, name="Aranestro", maxkp=68, typ=["Wasser","Käfer"], atk=70, defence=92, spatk=50, spdef=132, init=42, attacken=[], level=10, currentkp=68, fp=0, front_img=None, back_img=None):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Imantis(Pokemon):
    def __init__(self, name="Imantis", maxkp=40, typ=["Pflanze"], atk=55, defence=35, spatk=50, spdef=35, init=35, attacken=[], level=1, currentkp=40, fp=0, front_img=None, back_img=None):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Mantidea(Pokemon):
    def __init__(self, name="Mantidea", maxkp=70, typ=["Pflanze"], atk=105, defence=90, spatk=80, spdef=90, init=45, attacken=[], level=1, currentkp=70, fp=0, front_img=None, back_img=None):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Bubungus(Pokemon):
    def __init__(self, name="Bubungus", maxkp=50, typ=["Pflanze","Fee"], atk=35, defence=55, spatk=65, spdef=75, init=15, attacken=[], level=1, currentkp=50, fp=0, front_img=None, back_img=None):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Lamellux(Pokemon):
    def __init__(self, name="Lamellux", maxkp=60, typ=["Pflanze","Fee"], atk=75, defence=80, spatk=90, spdef=100, init=30, attacken=[], level=10, currentkp=60, fp=0, front_img=None, back_img=None):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Molunk(Pokemon):
    def __init__(self, name="Molunk", maxkp=48, typ=["Gift","Feuer"], atk=44, defence=40, spatk=71, spdef=40, init=77, attacken=[], level=1, currentkp=48, fp=0, front_img=None, back_img=None):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Amfira(Pokemon):
    def __init__(self, name="Amfira", maxkp=68, typ=["Gift","Feuer"], atk=64, defence=60, spatk=111, spdef=60, init=117, attacken=[], level=10, currentkp=68, fp=0, front_img=None, back_img=None):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Velursi(Pokemon):
    def __init__(self, name="Velursi", maxkp=70, typ=["Normal","Kampf"], atk=75, defence=50, spatk=45, spdef=50, init=50, attacken=[], level=1, currentkp=70, fp=0, front_img=None, back_img=None):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Kosturso(Pokemon):
    def __init__(self, name="Kosturso", maxkp=120, typ=["Normal","Kampf"], atk=125, defence=80, spatk=55, spdef=60, init=60, attacken=[], level=10, currentkp=120, fp=0, front_img=None, back_img=None):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Frubberl(Pokemon):
    def __init__(self, name="Frubberl", maxkp=42, typ=["Pflanze"], atk=30, defence=38, spatk=30, spdef=38, init=32, attacken=[], level=1, currentkp=42, fp=0, front_img=None, back_img=None):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Frubaila(Pokemon):
    def __init__(self, name="Frubaila", maxkp=52, typ=["Pflanze"], atk=40, defence=48, spatk=40, spdef=48, init=62, attacken=[], level=10, currentkp=52, fp=0, front_img=None, back_img=None):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Fruyal(Pokemon):
    def __init__(self, name="Fruyal", maxkp=72, typ=["Pflanze"], atk=120, defence=98, spatk=50, spdef=98, init=72, attacken=[], level=20, currentkp=72, fp=0, front_img=None, back_img=None):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Curelei(Pokemon):
    def __init__(self, name="Curelei", maxkp=51, typ=["Fee"], atk=52, defence=90, spatk=82, spdef=110, init=100, attacken=[], level=1, currentkp=51, fp=0, front_img=None, back_img=None):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Kommandutan(Pokemon):
    def __init__(self, name="Kommandutan", maxkp=90, typ=["Normal","Psycho"], atk=60, defence=80, spatk=90, spdef=110, init=60, attacken=[], level=1, currentkp=60, fp=0, front_img=None, back_img=None):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Quartermak(Pokemon):
    def __init__(self, name="Quartermak", maxkp=100, typ=["Kampf"], atk=120, defence=90, spatk=40, spdef=60, init=80, attacken=[], level=1, currentkp=100, fp=0, front_img=None, back_img=None):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Reißlaus(Pokemon):
    def __init__(self, name="Reißlaus", maxkp=25, typ=["Käfer","Wasser"], atk=25, defence=40, spatk=20, spdef=30, init=80, attacken=[], level=1, currentkp=25, fp=0, front_img=None, back_img=None):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Tectass(Pokemon):
    def __init__(self, name="Tectass", maxkp=75, typ=["Käfer","Wasser"], atk=125, defence=140, spatk=60, spdef=90, init=40, attacken=[], level=10, currentkp=75, fp=0, front_img=None, back_img=None):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Sankabuh(Pokemon):
    def __init__(self, name="Sankabuh", maxkp=55, typ=["Geist","Boden"], atk=55, defence=80, spatk=70, spdef=45, init=15, attacken=[], level=1, currentkp=55, fp=0, front_img=None, back_img=None):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Colossand(Pokemon):
    def __init__(self, name="Colossand", maxkp=85, typ=["Geist","Boden"], atk=75, defence=110, spatk=100, spdef=75, init=35, attacken=[], level=10, currentkp=85, fp=0, front_img=None, back_img=None):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Gufa(Pokemon):
    def __init__(self, name="Gufa", maxkp=55, typ=["Wasser"], atk=60, defence=130, spatk=30, spdef=130, init=5, attacken=[], level=1, currentkp=55, fp=0, front_img=None, back_img=None):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Typ_Null(Pokemon):
    def __init__(self, name="Typ:Null", maxkp=95, typ=["Normal"], atk=95, defence=95, spatk=95, spdef=95, init=59, attacken=[], level=1, currentkp=95, fp=0, front_img=None, back_img=None):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)


class Amigento(Pokemon):
    def __init__(self, name="Amigento", maxkp=95, typ=["Normal"], atk=95, defence=95, spatk=95, spdef=95, init=95, attacken=[], level=1, currentkp=95, fp=0, front_img=None, back_img=None):
        super().__init__(name, maxkp, typ, atk, defence, spatk, spdef, init, attacken, level, currentkp, fp, front_img, back_img)