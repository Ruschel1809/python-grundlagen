#---------------------------------------------------------------
# Dateiname: routenplanerSchnellsteRoute.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm findet den kürzesten Weg zwischen zwei Punkten
# Autor: Lena
# Letzte Änderung: 17.06.2025
#---------------------------------------------------------------

# Tiefensuche
#G={1:[2,4], 2:[1,3,5], 3:[2,5], 4:[1,5], 5:[4,2,3,6], 6:[5]}

#def suche_weg(aktuell, ziel, besucht):
#    besucht = besucht + [aktuell]
#    if aktuell == ziel:
#        return besucht
#    else:
#        for k in G[aktuell]:
#            if k not in besucht:
#                weg = suche_weg(k, ziel, besucht)
#                if weg:
#                    return weg
#        return []
#
#while True:
#    start = int(input("Start: "))
#    ende = int(input("Ziel: "))
#    route = suche_weg(start, ende, [])
#    print("Weg: ", route)

# Breitensuche

G = {1:[2,4], 2:[1,3,5], 3:[2,5], 4:[1,5], 5:[4,2,3,6], 6:[5]}

def finde_kuerzesten_weg(start, ziel):
    besucht = set()
    wege_nach_laenge = {0: [[start]]}  # Länge 0 = Startpunkt

    for laenge in range(1, len(G) + 1):  # maximal n-1 Schritte nötig
        wege_nach_laenge[laenge] = []
        for weg in wege_nach_laenge[laenge - 1]:
            letzter = weg[-1]
            if letzter == ziel:
                return weg  # Ziel erreicht
            if letzter not in besucht:
                besucht.add(letzter)
                for nachbar in G.get(letzter, []):
                    if nachbar not in weg:  # vermeide Zyklen
                        neuer_weg = weg + [nachbar]
                        if nachbar == ziel:
                            return neuer_weg
                        wege_nach_laenge[laenge].append(neuer_weg)
    return []  # Kein Weg gefunden

while True:
    start = int(input("Start: "))
    ende = int(input("Ziel: "))
    route = finde_kuerzesten_weg(start, ende)
    print("Kürzester Weg:", route)
