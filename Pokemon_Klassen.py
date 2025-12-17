# Pokemon
class Pokemon:
    def __init__(
                 self, name, typ, maxkp, atk, defence, spatk, spdef, init,
                 attacken=None, level=1, currentkp=None, fp=0,
                 front_img=None, back_img=None
                ):

        if attacken is None:
            attacken = []

        self.name = name
        self.typ = typ
        self.maxkp = maxkp
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
    def __init__(self, name="Bauz", typ=["Pflanze", "Flug"],
                 maxkp=68, atk=55, defence=55, spatk=50, spdef=50,
                 init=42, level=1, currentkp=68, attacken=[], fp=0,
                 front_img="front_bauz_img",
                 back_img="back_bauz_img"):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Arboretoss(Pokemon):
    def __init__(self, name="Arboretoss", typ=["Pflanze", "Flug"],
                 maxkp=78, atk=75, defence=75, spatk=70, spdef=70,
                 init=52, level=10, currentkp=78, attacken=[], fp=0,
                 front_img="front_arboretoss_img",
                 back_img="back_arboretoss_img"):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Silvarro(Pokemon):
    def __init__(self, name="Silvarro", typ=["Pflanze", "Geist"],
                 maxkp=78, atk=107, defence=75, spatk=100, spdef=100,
                 init=70, level=30, currentkp=78, attacken=[], fp=0,
                 front_img="front_silvarro_img",
                 back_img="back_silvarro_img"):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Flamiau(Pokemon):
    def __init__(self, name="Flamiau", typ=["Feuer"],
                 maxkp=45, atk=65, defence=40, spatk=60, spdef=40,
                 init=70, level=1, currentkp=45, attacken=[], fp=0,
                 front_img="front_flamiau_img",
                 back_img="back_flamiau_img"):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Miezunder(Pokemon):
    def __init__(self, name="Miezunder", typ=["Feuer"],
                 maxkp=65, atk=85, defence=50, spatk=80, spdef=50,
                 init=90, level=10, currentkp=65, attacken=[], fp=0,
                 front_img="front_miezunder_img",
                 back_img="back_miezunder_img"):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Fuegro(Pokemon):
    def __init__(self, name="Fuegro", typ=["Feuer", "Unlicht"],
                 maxkp=95, atk=115, defence=90, spatk=80, spdef=90,
                 init=60, level=20, currentkp=95, attacken=[], fp=0,
                 front_img="front_fuegro_img",
                 back_img="back_fuegro_img"):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Robball(Pokemon):
    def __init__(self, name="Robball", typ=["Wasser"],
                 maxkp=50, atk=50, defence=54, spatk=66, spdef=56,
                 init=40, level=1, currentkp=50, attacken=[], fp=0,
                 front_img="front_robball_img",
                 back_img="back_robball_img"):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Marikeck(Pokemon):
    def __init__(self, name="Marikeck", typ=["Wasser"],
                 maxkp=60, atk=69, defence=69, spatk=91, spdef=81,
                 init=50, level=10, currentkp=60, attacken=[], fp=0,
                 front_img="front_marikeck_img",
                 back_img="back_marikeck_img"):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Primarene(Pokemon):
    def __init__(self, name="Primarene", typ=["Wasser", "Fee"],
                 maxkp=80, atk=74, defence=74, spatk=126, spdef=116,
                 init=60, level=20, currentkp=80, attacken=[], fp=0,
                 front_img="front_primarene_img",
                 back_img="back_primarene_img"):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Peppeck(Pokemon):
    def __init__(self, name="Peppeck", typ=["Normal", "Flug"],
                 maxkp=35, atk=75, defence=30, spatk=30, spdef=30,
                 init=65, level=1, currentkp=35, attacken=[], fp=0,
                 front_img="front_peppeck_img",
                 back_img="back_peppeck_img"):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Trompeck(Pokemon):
    def __init__(self, name="Trompeck", typ=["Normal", "Flug"],
                 maxkp=55, atk=85, defence=50, spatk=40, spdef=50,
                 init=75, level=10, currentkp=55, attacken=[], fp=0,
                 front_img="front_trompeck_img",
                 back_img="back_trompeck_img"):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Tukanon(Pokemon):
    def __init__(self, name="Tukanon", typ=["Normal", "Flug"],
                 maxkp=80, atk=120, defence=75, spatk=75, spdef=75,
                 init=60, level=20, currentkp=80, attacken=[], fp=0,
                 front_img="front_tukanon_img",
                 back_img="back_tukanon_img"):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Mangunior(Pokemon):
    def __init__(self, name="Mangunior", typ=["Normal"],
                 maxkp=48, atk=70, defence=30, spatk=30, spdef=30,
                 init=45, level=1, currentkp=48, attacken=[], fp=0,
                 front_img="front_mangunior_img",
                 back_img="back_mangunior_img"):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Manguspektor(Pokemon):
    def __init__(self, name="Manguspektor", typ=["Normal"],
                 maxkp=88, atk=110, defence=60, spatk=55, spdef=60,
                 init=45, level=10, currentkp=88, attacken=[], fp=0,
                 front_img="front_manguspektor_img",
                 back_img="back_manguspektor_img"):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Mabula(Pokemon):
    def __init__(self, name="Mabula", typ=["Käfer"],
                 maxkp=47, atk=62, defence=45, spatk=55, spdef=45,
                 init=46, level=1, currentkp=47, attacken=[], fp=0,
                 front_img="front_mabula_img",
                 back_img="back_mabula_img"):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Akkup(Pokemon):
    def __init__(self, name="Akkup", typ=["Käfer","Elektro"],
                 maxkp=57, atk=82, defence=95, spatk=55, spdef=75,
                 init=36, level=10, currentkp=57, attacken=[], fp=0,
                 front_img="front_akkup_img",
                 back_img="back_akupp_img"):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Donarion(Pokemon):
    def __init__(self, name="Donarion", typ=["Käfer","Elektro"],
                 maxkp=77, atk=70, defence=90, spatk=145, spdef=75,
                 init=43, level=20, currentkp=77, attacken=[], fp=0,
                 front_img="front_donarion_img",
                 back_img="back_donarion_img"):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Krabbox(Pokemon):
    def __init__(self, name="Krabbox", typ=["Kampf"],
                 maxkp=47, atk=82, defence=57, spatk=42, spdef=47,
                 init=63, level=1, currentkp=47, attacken=[], fp=0,
                 front_img="front_krabbox_img",
                 back_img="back_krabbox_img"):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Krawell(Pokemon):
    def __init__(self, name="Krawell", typ=["Kampf", "Eis"],
                 maxkp=97, atk=132, defence=77, spatk=62, spdef=67,
                 init=43, level=10, currentkp=97, attacken=[], fp=0,
                 front_img="front_krawell_img",
                 back_img="back_krawell_img"):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Wommel(Pokemon):
    def __init__(self, name="Wommel", typ=["Käfer","Fee"],
                 maxkp=40, atk=45, defence=40, spatk=55, spdef=40,
                 init=84, level=1, currentkp=40, attacken=[], fp=0,
                 front_img="front_wommel_img",
                 back_img="back_wommel_img"):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Bandelby(Pokemon):
    def __init__(self, name="Bandelby", typ=["Käfer","Fee"],
                 maxkp=60, atk=55, defence=60, spatk=95, spdef=70,
                 init=124, level=10, currentkp=60, attacken=[], fp=0,
                 front_img="front_bandelby_img",
                 back_img="back_bandelby_img"):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Garstella(Pokemon):
    def __init__(self, name="Garstella", typ=["Gift","Wasser"],
                 maxkp=50, atk=53, defence=62, spatk=43, spdef=52,
                 init=45, level=1, currentkp=50, attacken=[], fp=0,
                 front_img=None,
                 back_img=None):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Aggrostella(Pokemon):
    def __init__(self, name="Aggrostella", typ=["Gift","Wasser"],
                 maxkp=50, atk=63, defence=152, spatk=53, spdef=142,
                 init=35, level=10, currentkp=50, attacken=[], fp=0,
                 front_img=None,
                 back_img=None):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Pampuli(Pokemon):
    def __init__(self, name="Pampuli", typ=["Boden"],
                 maxkp=70, atk=100, defence=70, spatk=45, spdef=70,
                 init=45, level=1, currentkp=70, attacken=[], fp=0,
                 front_img=None,
                 back_img=None):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Pampross(Pokemon):
    def __init__(self, name="Pampross", typ=["Boden"],
                 maxkp=100, atk=125, defence=100, spatk=55, spdef=85,
                 init=35, level=10, currentkp=100, attacken=[], fp=0,
                 front_img=None,
                 back_img=None):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Araqua(Pokemon):
    def __init__(self, name="Araqua", typ=["Wasser","Käfer"],
                 maxkp=38, atk=40, defence=52, spatk=40, spdef=72,
                 init=27, level=1, currentkp=38, attacken=[], fp=0,
                 front_img=None,
                 back_img=None):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Aranestro(Pokemon):
    def __init__(self, name="Aranestro", typ=["Wasser","Käfer"],
                 maxkp=68, atk=70, defence=92, spatk=50, spdef=132,
                 init=42, level=10, currentkp=68, attacken=[], fp=0,
                 front_img=None,
                 back_img=None):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Imantis(Pokemon):
    def __init__(self, name="Imantis", typ=["Pflanze"],
                 maxkp=40, atk=55, defence=35, spatk=50, spdef=35,
                 init=35, level=1, currentkp=40, attacken=[], fp=0,
                 front_img=None,
                 back_img=None):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Mantidea(Pokemon):
    def __init__(self, name="Mantidea", typ=["Pflanze"],
                 maxkp=70, atk=105, defence=90, spatk=80, spdef=90,
                 init=45, level=1, currentkp=70, attacken=[], fp=0,
                 front_img=None,
                 back_img=None):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Bubungus(Pokemon):
    def __init__(self, name="Bubungus", typ=["Pflanze","Fee"],
                 maxkp=50, atk=35, defence=55, spatk=65, spdef=75,
                 init=15, level=1, currentkp=50, attacken=[], fp=0,
                 front_img=None,
                 back_img=None):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Lamellux(Pokemon):
    def __init__(self, name="Lamellux", typ=["Pflanze","Fee"],
                 maxkp=60, atk=75, defence=80, spatk=90, spdef=100,
                 init=30, level=10, currentkp=60, attacken=[], fp=0,
                 front_img=None,
                 back_img=None):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Molunk(Pokemon):
    def __init__(self, name="Molunk", typ=["Gift","Feuer"],
                 maxkp=48, atk=44, defence=40, spatk=71, spdef=40,
                 init=77, level=1, currentkp=48, attacken=[], fp=0,
                 front_img=None,
                 back_img=None):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Amfira(Pokemon):
    def __init__(self, name="Amfira", typ=["Gift","Feuer"],
                 maxkp=68, atk=64, defence=60, spatk=111, spdef=60,
                 init=117, level=10, currentkp=68, attacken=[], fp=0,
                 front_img=None,
                 back_img=None):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Velursi(Pokemon):
    def __init__(self, name="Velursi", typ=["Normal","Kampf"],
                 maxkp=70, atk=75, defence=50, spatk=45, spdef=50,
                 init=50, level=1, currentkp=70, attacken=[], fp=0,
                 front_img=None,
                 back_img=None):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Kosturso(Pokemon):
    def __init__(self, name="Kosturso", typ=["Normal","Kampf"],
                 maxkp=120, atk=125, defence=80, spatk=55, spdef=60,
                 init=60, level=10, currentkp=120, attacken=[], fp=0,
                 front_img=None,
                 back_img=None):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Frubberl(Pokemon):
    def __init__(self, name="Frubberl", typ=["Pflanze"],
                 maxkp=42, atk=30, defence=38, spatk=30, spdef=38,
                 init=32, level=1, currentkp=42, attacken=[], fp=0,
                 front_img=None,
                 back_img=None):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Frubaila(Pokemon):
    def __init__(self, name="Frubaila", typ=["Pflanze"],
                 maxkp=52, atk=40, defence=48, spatk=40, spdef=48,
                 init=62, level=10, currentkp=52, attacken=[], fp=0,
                 front_img=None,
                 back_img=None):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Fruyal(Pokemon):
    def __init__(self, name="Fruyal", typ=["Pflanze"],
                 maxkp=72, atk=120, defence=98, spatk=50, spdef=98,
                 init=72, level=20, currentkp=72, attacken=[], fp=0,
                 front_img=None,
                 back_img=None):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Curelei(Pokemon):
    def __init__(self, name="Curelei", typ=["Fee"],
                 maxkp=51, atk=52, defence=90, spatk=82, spdef=110,
                 init=100, level=1, currentkp=51, attacken=[], fp=0,
                 front_img=None,
                 back_img=None):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Kommandutan(Pokemon):
    def __init__(self, name="Kommandutan", typ=["Normal","Psycho"],
                 maxkp=90, atk=60, defence=80, spatk=90, spdef=110,
                 init=60, level=1, currentkp=60, attacken=[], fp=0,
                 front_img=None,
                 back_img=None):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Quartermak(Pokemon):
    def __init__(self, name="Quartermak", typ=["Kampf"],
                 maxkp=100, atk=120, defence=90, spatk=40, spdef=60,
                 init=80, level=1, currentkp=100, attacken=[], fp=0,
                 front_img=None,
                 back_img=None):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Reißlaus(Pokemon):
    def __init__(self, name="Reißlaus", typ=["Käfer","Wasser"],
                 maxkp=25, atk=25, defence=40, spatk=20, spdef=30,
                 init=80, level=1, currentkp=25, attacken=[], fp=0,
                 front_img=None,
                 back_img=None):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Tectass(Pokemon):
    def __init__(self, name="Tectass", typ=["Käfer","Wasser"],
                 maxkp=75, atk=125, defence=140, spatk=60, spdef=90,
                 init=40, level=10, currentkp=75, attacken=[], fp=0,
                 front_img=None,
                 back_img=None):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Sankabuh(Pokemon):
    def __init__(self, name="Sankabuh", typ=["Geist","Boden"],
                 maxkp=55, atk=55, defence=80, spatk=70, spdef=45,
                 init=15, level=1, currentkp=55, attacken=[], fp=0,
                 front_img=None,
                 back_img=None):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Colossand(Pokemon):
    def __init__(self, name="Colossand", typ=["Geist","Boden"],
                 maxkp=85, atk=75, defence=110, spatk=100, spdef=75,
                 init=35, level=10, currentkp=85, attacken=[], fp=0,
                 front_img=None,
                 back_img=None):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Gufa(Pokemon):
    def __init__(self, name="Gufa", typ=["Wasser"],
                 maxkp=55, atk=60, defence=130, spatk=30, spdef=130,
                 init=5, level=1, currentkp=55, attacken=[], fp=0,
                 front_img=None,
                 back_img=None):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Typ_Null(Pokemon):
    def __init__(self, name="Typ:Null", typ=["Normal"],
                 maxkp=95, atk=95, defence=95, spatk=95, spdef=95,
                 init=59, level=1, currentkp=95, attacken=[], fp=0,
                 front_img=None,
                 back_img=None):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)


class Amigento(Pokemon):
    def __init__(self, name="Amigento", typ=["Normal"],
                 maxkp=95, atk=95, defence=95, spatk=95, spdef=95,
                 init=95, level=1, currentkp=95, attacken=[], fp=0,
                 front_img=None,
                 back_img=None):
        super().__init__(name, typ, maxkp, atk, defence, spatk, spdef, init,
                         attacken, level, currentkp, fp, front_img, back_img)