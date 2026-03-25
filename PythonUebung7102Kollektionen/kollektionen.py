#---------------------------------------------------------------
# Dateiname: kollektionen.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm macht schlaue Sachen mit Kollektionen
# Autor: Lena
# Letzte Änderung: 16.06.2025
#---------------------------------------------------------------

import math as m, random as r

def erzeuge_zufallszahlen_liste(anzahl: int, max_wert : int) -> list[int]:
    """Erzeugt eine Liste von Zufallszahlen."""
    return [r.randint(1, max_wert + 1) for _ in range(anzahl)]

def berechne_durchschnitt (zahlen_liste : list[int]) -> float:
    """Berechnet den Durchschnitt der Zahlen in der Liste."""
    if not zahlen_liste:
        return 0.0
    return sum(zahlen_liste) / len(zahlen_liste)

def sortiere_und_teile(liste_von_zahlen : list[int]) -> tuple[list[int], list[int]]:
   laenge_liste = len(liste_von_zahlen)
   liste_von_zahlen.sort()
   if laenge_liste == 0:
       return ([], [])
   return (liste_von_zahlen[:laenge_liste//2] if laenge_liste % 2 == 0 else liste_von_zahlen[:(laenge_liste//2 + 1)], liste_von_zahlen[laenge_liste//2:] if laenge_liste % 2 == 0 else liste_von_zahlen[(laenge_liste//2 + 1):])

print("Liste von Zufallszahlen: ",erzeuge_zufallszahlen_liste(10, 100))
print("Durchschnitt der Zahlen: ", berechne_durchschnitt(erzeuge_zufallszahlen_liste(10, 100)))
print("Sortierte und geteilte Liste: ",sortiere_und_teile(erzeuge_zufallszahlen_liste(10, 100)))