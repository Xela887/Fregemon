class Attacke:
    def __init__(self, atkdmg, typ, dmgtype):
        self.atkdmg = atkdmg
        self.typ = typ
        self.dmgtype = dmgtype


class Kratzer(Attacke):
    def __init__(self):
        super().__init__(40, "Normal", "physisch")

class Sternschauer(Attacke):
    def __init__(self):
        super().__init__(60, "Normal", "spezial")

class Schallwelle(Attacke):
    def __init__(self):
        super().__init__(90, "Normal", "spezial")

class Risikotackle(Attacke):
    def __init__(self):
        super().__init__(120, "Normal", "physisch")


class Ableithieb(Attacke):
    def __init__(self):
        super().__init__(75, "Kampf", "physisch")

class Durchbruch(Attacke):
    def __init__(self):
        super().__init__(75, "Kampf", "physisch")

class Fußtritt(Attacke):
    def __init__(self):
        super().__init__(65, "Kampf", "physisch")

class Fokusstoß(Attacke):
    def __init__(self):
        super().__init__(120, "Kampf", "spezial")


class Pflücker(Attacke):
    def __init__(self):
        super().__init__(60, "Flug", "physisch")

class Orkan(Attacke):
    def __init__(self):
        super().__init__(110, "Flug", "spezial")

class Fliegen(Attacke):
    def __init__(self):
        super().__init__(90, "Flug", "physisch")

class Akrobatik(Attacke):
    def __init__(self):
        super().__init__(55, "Flug", "physisch")


class Giftschock(Attacke):
    def __init__(self):
        super().__init__(65, "Gift", "spezial")

class Matschbombe(Attacke):
    def __init__(self):
        super().__init__(90, "Gift", "spezial")

class Giftzahn(Attacke):
    def __init__(self):
        super().__init__(50, "Gift", "physisch")

class Schlammwoge(Attacke):
    def __init__(self):
        super().__init__(95, "Gift", "spezial")


class Lehmschuss(Attacke):
    def __init__(self):
        super().__init__(50, "Boden", "spezial")

class Dampfwalze(Attacke):
    def __init__(self):
        super().__init__(60, "Boden", "physisch")

class Schaufler(Attacke):
    def __init__(self):
        super().__init__(80, "Boden", "physisch")

class Erdbeben(Attacke):
    def __init__(self):
        super().__init__(100, "Boden", "physisch")


class Felsgrab(Attacke):
    def __init__(self):
        super().__init__(60, "Gestein", "physisch")

class Steinhagel(Attacke):
    def __init__(self):
        super().__init__(75, "Gestein", "physisch")

class Juwelenkraft(Attacke):
    def __init__(self):
        super().__init__(80, "Gestein", "spezial")

class Steinkante(Attacke):
    def __init__(self):
        super().__init__(100, "Gestein", "physisch")


class Käfertrutz(Attacke):
    def __init__(self):
        super().__init__(50, "Käfer", "spezial")

class Blutsauger(Attacke):
    def __init__(self):
        super().__init__(80, "Käfer", "physisch")

class Kehrtwende(Attacke):
    def __init__(self):
        super().__init__(70, "Käfer", "physisch")

class Pollenknödel(Attacke):
    def __init__(self):
        super().__init__(90, "Käfer", "spezial")


class Phantomkraft(Attacke):
    def __init__(self):
        super().__init__(90, "Geist", "physisch")

class Erstauner(Attacke):
    def __init__(self):
        super().__init__(30, "Geist", "physisch")

class Spukball(Attacke):
    def __init__(self):
        super().__init__(80, "Geist", "spezial")

class Unheilböen(Attacke):
    def __init__(self):
        super().__init__(60, "Geist", "spezial")


class Lichtkanone(Attacke):
    def __init__(self):
        super().__init__(80, "Stahl", "spezial")

class Gigantenhieb(Attacke):
    def __init__(self):
        super().__init__(100, "Stahl", "physisch")

class Eisenschädel(Attacke):
    def __init__(self):
        super().__init__(80, "Stahl", "physisch")

class TachyonSchnitt(Attacke):
    def __init__(self):
        super().__init__(100, "Stahl", "spezial")


class Feuerzahn(Attacke):
    def __init__(self):
        super().__init__(65, "Feuer", "physisch")

class Flammenwurf(Attacke):
    def __init__(self):
        super().__init__(90, "Feuer", "spezial")

class Einäschern(Attacke):
    def __init__(self):
        super().__init__(60, "Feuer", "spezial")

class Lohekanonade(Attacke):
    def __init__(self):
        super().__init__(150, "Feuer", "spezial")

class Flammenblitz(Attacke):
    def __init__(self):
        super().__init__(120, "Feuer", "physisch")


class Wasserdüse(Attacke):
    def __init__(self):
        super().__init__(40, "Wasser", "physisch")

class KalteDusche(Attacke):
    def __init__(self):
        super().__init__(50, "Wasser", "spezial")

class Lehmbrühe(Attacke):
    def __init__(self):
        super().__init__(90, "Wasser", "spezial")

class Surfer(Attacke):
    def __init__(self):
        super().__init__(90, "Wasser", "spezial")


class Rasierblatt(Attacke):
    def __init__(self):
        super().__init__(55, "Pflanze", "physisch")

class Blattwerk(Attacke):
    def __init__(self):
        super().__init__(40, "Pflanze", "physisch")

class Gigasauger(Attacke):
    def __init__(self):
        super().__init__(75, "Pflanze", "spezial")

class Strauchler(Attacke):
    def __init__(self):
        super().__init__(75, "Pflanze", "spezial")


class Ladestrahl(Attacke):
    def __init__(self):
        super().__init__(50, "Elektro", "spezial")

class Ladungsstoß(Attacke):
    def __init__(self):
        super().__init__(80, "Elektro", "spezial")

class Donnerschlag(Attacke):
    def __init__(self):
        super().__init__(75, "Elektro", "physisch")

class Kreuzdonner(Attacke):
    def __init__(self):
        super().__init__(100, "Elektro", "physisch")


class Psychobeißer(Attacke):
    def __init__(self):
        super().__init__(85, "Psycho", "physisch")

class Konfusion(Attacke):
    def __init__(self):
        super().__init__(50, "Psycho", "spezial")

class Flächenmacht(Attacke):
    def __init__(self):
        super().__init__(80, "Psycho", "spezial")

class Psychoschneide(Attacke):
    def __init__(self):
        super().__init__(80, "Psycho", "physisch")


class Eissturm(Attacke):
    def __init__(self):
        super().__init__(55, "Eis", "spezial")

class Eishammer(Attacke):
    def __init__(self):
        super().__init__(100, "Eis", "physisch")

class Eisstrahl(Attacke):
    def __init__(self):
        super().__init__(90, "Eis", "spezial")

class Blizzardlanze(Attacke):
    def __init__(self):
        super().__init__(130, "Eis", "physisch")


class Wutanfall(Attacke):
    def __init__(self):
        super().__init__(120, "Drache", "physisch")

class Drachenrute(Attacke):
    def __init__(self):
        super().__init__(60, "Drache", "physisch")

class Raumschlag(Attacke):
    def __init__(self):
        super().__init__(100, "Drache", "spezial")

class Schuppenrasseln(Attacke):
    def __init__(self):
        super().__init__(110, "Drache", "spezial")


class Biss(Attacke):
    def __init__(self):
        super().__init__(60, "Unlicht", "physisch")

class Kniefalltrick(Attacke):
    def __init__(self):
        super().__init__(80, "Unlicht", "physisch")

class Klingenschwall(Attacke):
    def __init__(self):
        super().__init__(65, "Unlicht", "physisch")

class Finsteraura(Attacke):
    def __init__(self):
        super().__init__(80, "Unlicht", "spezial")


class Nebelexplosion(Attacke):
    def __init__(self):
        super().__init__(100, "Fee", "spezial")

class Zauberschein(Attacke):
    def __init__(self):
        super().__init__(80, "Fee", "spezial")

class Zauberturbo(Attacke):
    def __init__(self):
        super().__init__(100, "Fee", "physisch")

class Knuddler(Attacke):
    def __init__(self):
        super().__init__(90, "Fee", "physisch")
