from Angriff_Klassen import Attacken
from Trainer_Klasse import Spieler
from Altar_Klasse import Altar_For_Sacrifices
from Pokemon_Klassen import Pokemon
from tkinter import filedialog
import os
import json


def save(name: str, pokemonliste: list, altar: Altar_For_Sacrifices, pokemon_team: list):
    if name == "":
        name = "fregen"
    dateiname = f"{name}.json"

    daten = {
        "pokemon" : [],
        "altar" : [],
        "pokemon_team" : []
    }
    
    for pokemon in pokemonliste:
        daten["pokemon"].append({
            "name" : pokemon.name,
            "typ": pokemon.typ,
            "level" : pokemon.level,
            "ep" : pokemon.ep,
            "maxkp" : pokemon.maxkp,
            "atk" : pokemon.atk,
            "defence" : pokemon.defence,
            "spatk" : pokemon.spatk,
            "spdef" : pokemon.spdef,
            "init" : pokemon.init,
            "currentkp" : pokemon.currentkp,
            "attacke_physic" : pokemon.attacken[0].__class__.__name__,
            "attacke_special": pokemon.attacken[1].__class__.__name__,
            "fp" : pokemon.fp,
            "front_img" : pokemon.front_img,
            "back_img" : pokemon.back_img
        })

    daten["altar"].append({
        "pokemon_bodies" : altar.pokemon_bodies,
        "trainer_bodies" : altar.trainer_bodies,
        "sacrifice_count" : altar.sacrifice_count,
        "fp_amount" : altar.fp_amount
    })

    for pokemon in pokemon_team:
        daten["pokemon_team"].append({
            "name": pokemon.name,
            "typ": pokemon.typ,
            "level": pokemon.level,
            "ep" : pokemon.ep,
            "maxkp": pokemon.maxkp,
            "atk": pokemon.atk,
            "defence": pokemon.defence,
            "spatk": pokemon.spatk,
            "spdef": pokemon.spdef,
            "init": pokemon.init,
            "currentkp": pokemon.currentkp,
            "attacke_physic": pokemon.attacken[0].__class__.__name__,
            "attacke_special": pokemon.attacken[1].__class__.__name__,
            "fp": pokemon.fp,
            "front_img": pokemon.front_img,
            "back_img": pokemon.back_img
        })

    try:
        with open(dateiname, "w", encoding="utf-8") as f:
            json.dump(daten, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Fehler beim Speichern: {e}")

def load(Attacken=Attacken):
    dateipfad = filedialog.askopenfilename(
        title="Datei auswählen",
        filetypes=(("JSON-Dateien", "*.json"), ("Alle Dateien", "*.*"))
    )

    name = os.path.splitext(os.path.basename(dateipfad))[0]

    pokemonliste = []
    pokemon_team = []

    try:
        with open(dateipfad, "r", encoding="utf-8") as f:
            daten = json.load(f)
    except FileNotFoundError:
        print(f"Datei {dateipfad} nicht gefunden.")
        return [], []
    except json.JSONDecodeError:
        print(f"Fehler beim Lesen der JSON-Datei.")
        return [], []

    for p in daten.get("pokemon", []):
        cls = Pokemon.registry.get(p["name"], Pokemon)

        pokemon = cls(
            p["name"],
            p["typ"],
            p["maxkp"],
            p["atk"],
            p["defence"],
            p["spatk"],
            p["spdef"],
            p["init"],
            p["level"],
            p["currentkp"],
            [p["attacke_physic"], p["attacke_special"]],
            p["fp"],
            p["front_img"],
            p["back_img"])
        pokemon.ep = p["ep"]
        for poke in pokemonliste:
            if pokemon.name == poke.name:
                pokemon = poke
        for atk in Attacken:
            if pokemon.attacken[0] == atk().__class__.__name__:
                pokemon.attacken[0] = atk()
        for atk in Attacken:
            if pokemon.attacken[1] == atk().__class__.__name__:
                pokemon.attacken[1] = atk()
        pokemonliste.append(pokemon)

    for p in daten.get("pokemon_team", []):
        cls = Pokemon.registry.get(p["name"], Pokemon)

        pokemon = cls(
            p["name"],
            p["typ"],
            p["maxkp"],
            p["atk"],
            p["defence"],
            p["spatk"],
            p["spdef"],
            p["init"],
            p["level"],
            p["currentkp"],
            [p["attacke_physic"], p["attacke_special"]],
            p["fp"],
            p["front_img"],
            p["back_img"])
        pokemon.ep = p["ep"]
        for poke in pokemonliste:
            if pokemon.name == poke.name:
                pokemon = poke
        for atk in Attacken:
            if pokemon.attacken[0] == atk().__class__.__name__:
                pokemon.attacken[0] = atk()
        for atk in Attacken:
            if pokemon.attacken[1] == atk().__class__.__name__:
                pokemon.attacken[1] = atk()
        pokemon_team.append(pokemon)

    spieler = Spieler(name, pokemonliste, pokemon_team[0], pokemon_team)

    for a in daten.get("altar", []):
        altar = Altar_For_Sacrifices(spieler,
                                     a["pokemon_bodies"],
                                     a["trainer_bodies"],
                                     a["fp_amount"],
                                     a["sacrifice_count"])

    return spieler, altar