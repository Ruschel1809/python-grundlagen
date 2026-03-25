#---------------------------------------------------------------
# Dateiname: routenplanerSchnellsteRoute.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm implementiert verschiedene Funktionen die randint und sqrt verwenden
# Autor: Lena
# Letzte Änderung: 17.06.2025
#---------------------------------------------------------------

from random import randint
from math import sqrt

def erzeuge_zufallszahlen_liste(anzahl:int)-> list:
    return list(randint(1, 100) for x in range(1, anzahl + 1))

def berechne_wurzeln(zahlen_liste:list) -> list:
    return [sqrt(x) for x in zahlen_liste]

def sortiere_und_erzeuge_tupel(quadratwurzel_liste:list) -> list[tuple]:
    quadratwurzel_liste.sort()
    tupel_liste = []
    for x in quadratwurzel_liste:
        tupel_liste.append((round(x**2), x))
    return tupel_liste

def erstelle_dictionary(tupel_liste:list) -> dict[int, float]:
    dictionary = {}
    for x , y in tupel_liste:
        dictionary[x] = y
    return dictionary

def main():
    anzahl = 10
    print(f"Zufallsliste: {erzeuge_zufallszahlen_liste(anzahl)}")
    print(f"Quadratwurzelliste: {berechne_wurzeln(erzeuge_zufallszahlen_liste(anzahl))}")
    print(f"sortierte Liste: {sortiere_und_erzeuge_tupel(berechne_wurzeln(erzeuge_zufallszahlen_liste(anzahl)))}")
    print(f"Dictionary: {erstelle_dictionary(sortiere_und_erzeuge_tupel(berechne_wurzeln(erzeuge_zufallszahlen_liste(anzahl))))}")

main()

