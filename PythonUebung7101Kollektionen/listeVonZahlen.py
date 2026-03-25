#---------------------------------------------------------------
# Dateiname: listeVonZahlen.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm erzeugt eine Liste von Zahlen und wendet verschiedete Funktionen darauf an
# Autor: Lena
# Letzte Änderung: 16.06.2025
#---------------------------------------------------------------

import random as r

def erzeugeListeVonZehnZufallszahlen() -> list[int]:
    """Erzeugt eine Liste von 10 Zufallszahlen zwischen 1 und 100."""
    return [r.randint(1, 100) for _ in range(10)]

def sortiere_und_zaehle(liste: list[int]) -> int:
    """Sortiert die Liste und gibt der Anzahl der Elemente zurück."""
    liste.sort()
    anzahlListenElemente = len(liste)

    if anzahlListenElemente > 5:
        print("Mehr als 5 Elemente in der Liste:")
    else:
        print("5 oder weniger Elemente in der Liste:")
    return anzahlListenElemente

def erzeuge_quadrat_zu_jeder_zahl(liste: list[int]) -> list[(int,int)]:
    """Erzeugt eine Liste, die Tupel aus der Zahl und ihrem Quadrat enthält."""
    return [(zahl, zahl ** 2) for zahl in liste]

def drucke_liste(liste: list[(int,int)]) -> None:
    """Druckt die Liste von Tupeln."""
    for zahl, quadrat in liste:
        print(f"Die Zahl {zahl} hat das Quadrat {quadrat}")

if __name__ == "__main__":
    # Erzeuge eine Liste von 10 Zufallszahlen
    zufallszahlen = erzeugeListeVonZehnZufallszahlen()
    print("Zufallszahlen:", zufallszahlen)

    # Sortiere die Liste und zähle die Elemente
    anzahl = sortiere_und_zaehle(zufallszahlen)
    print(f"Anzahl der Elemente in der Liste: {anzahl}")

    # Erzeuge eine Liste von Tupeln mit Zahl und Quadrat
    quadrate = erzeuge_quadrat_zu_jeder_zahl(zufallszahlen)
    print("Liste von Zahlen und ihren Quadraten:")
    
    # Drucke die Liste von Tupeln
    drucke_liste(quadrate)