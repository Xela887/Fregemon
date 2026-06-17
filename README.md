# Fregemon

## Inhaltsverzeichnis

1. [Beschreibung](#beschreibung)
2. [Features](#features)
3. [Technologien](#technologien)
4. [Installierung](#installierung)
5. [Benutzung](#benutzung)
6. [Speichern und Laden](#speichern-und-laden-des-spielfortschritts)

## Beschreibung

Ein kleines Spiel, falls man langeweile hat.

## Features

- Kämpfe gegen Gegner  
- Fregemon hochleveln  
- Stats der Fregemon verbessern  
- Neue Fregemon sammeln  
- Fregemon entwickeln  
- Deine besiegten Gegner opfern (haha)

## Technologien

Python 3.13  
Pygame 2.6.1

## Installierung

Neuste Version des GitHub Repositories (main Branch) klonen oder eine Zip des Projekts herunterladen und dann die alle Dateien extrahieren. Falls nicht vorhanden, [benutzte Technologien installieren](#benutze-technolgien-installieren).

### Benutze Technolgien installieren

Python installieren: Entweder im Microsoft Store installieren oder über https://www.python.org.  
Pygame installieren: Der einfachste Weg ist in die Konsole/Terminal das einzugeben.  

    pip install pygame  

## Benutzung

Entweder man startet "main.py" in einer IDE wie Visual Studio Code (https://code.visualstudio.com/download) oder man startet es über das installierte Python in der Konsole/Terminal. Dafür geht man zuerst mit cd in das Verzeichnis wo "main.py" liegt. Beispiel:

    cd C:/users/deinuser/dokumente/Fregemon

Dafür kann man einfach im Datei Explorer oben in der Adressleiste mit einem Rechtsklick die Adresse kopieren, wenn man im Ordner von Fregemon ist. Nun muss man nur noch diesen Befehl ausführen und das Programm startet dann.

    python main.py

## Speichern und laden des Spielfortschritts

Der Spielstand kann gespeichert werden indem man im Hauptmenü auf "Speichern" klickt, dies erstellt eine Datei spielername.json im lokalen Ordner. Diese kann geladen werden indem man beim Spielstart die Option "Spielstand laden" wählt und seinen Spielstand auswählt, also seine spielername.json Datei auswählt.

