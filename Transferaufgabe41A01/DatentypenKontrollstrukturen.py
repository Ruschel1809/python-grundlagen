#---------------------------------------------------------------
# Dateiname: DatenTypenKontrollstrukturen.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm macht schlaue Sachen.
# Autor: Lena
# Letzte Änderung: 05.06.2025
#---------------------------------------------------------------
def tupelListeErstellen():

    tupelListe = [("a",1), ("b",2), ("c",3), ("d",4), ("e",5)]
    ausgabe = ""
    nutzerTupel = input("Bitte geben Sie ein Tupel im Format (x,y) ein, wobei x ein Buchstabe und y eine Ganzzahl ist: ")
    for tupel in tupelListe:
        if nutzerTupel == tupel:
            ausgabe = "Das Element " + str(nutzerTupel) + " wurde gefunden."
            break
        else:
            ausgabe = "Das Element " + str(nutzerTupel) + " ist nicht vorhanden."
    print(ausgabe)

def zahlenUmwandeln():
    zeichenkette = "0123456789" #eine Zeichenkette zu casten, weil es die Aufgabenstelluzng verlangt
    eingabe = input("Bitte geben Sie eine Zahl ein,nach der in der Liste gesucht werden soll: ").lower()  # Eingabeaufforderung für den Benutzer
    
    
    if '-' in eingabe:  # Überprüfung, ob ein Minuszeichen in der Eingabe enthalten ist
        print(f'Die Eingabe "{eingabe}" ist eine negative Zahl, die Zahlenliste enthält nur positive Ganzzahlen.')
    elif '.' in eingabe:
        eingabe = float(eingabe)
        print(f'Die Eingabe "{eingabe}" ist eine Gleitkommazahl, die Zahlenliste enthält nur Ganzzahlen.')  # Ausgabe, wenn die Eingabe kein Integer ist
    else:
        eingabe = int(eingabe)  # Umwandlung der Eingabe in eine Ganzzahl
        if eingabe in zeichenkette:
            print(f'Die Eingabe "{eingabe}" ist in der Zahlenliste enthalten.')  # Ausgabe, wenn die Eingabe in der Liste enthalten ist
        
zahlenUmwandeln()


#MUSTERLÖSUNG
# a) Liste von Tupeln erstellen

elemente = [('A', 1), ('B', 2), ('C', 3), ('D', 4), ('E', 5)]
# b) Funktion, um zu prüfen, ob ein Element in der Liste vorhanden ist

def pruefe_element(buchstabe, zahl):
    if (buchstabe, zahl) in elemente:
        print(f"Element gefunden: ({buchstabe}, {zahl})")
    else:
        print("Element nicht gefunden.")
# c) Funktion, um Zeichenkette in Zahl umzuwandeln

def zeichenkette_in_zahl(zeichenkette):
    zahl = int(zeichenkette)
    print(f"Umwandlung erfolgreich: {zahl}")
    return zahl
# d) Kommentare im Code

# Die Funktion 'pruefe_element' überprüft, ob ein spezifisches Tupel in der Liste 'elemente' vorhanden ist.

# Die Funktion 'zeichenkette_in_zahl' versucht, eine Eingabe von einer Zeichenkette in eine ganze Zahl umzuwandeln.

# e) Benutzerschnittstelle

while True:
    aktion = input("Wähle eine Aktion: 'suchen', 'umwandeln' oder 'beenden': ")
    if aktion == 'suchen':
        buchstabe = input("Gib den Buchstaben des Elements ein: ")
        zahl = int(input("Gib die Zahl des Elements ein: "))
        pruefe_element(buchstabe, zahl)
    elif aktion == 'umwandeln':
        zeichenkette = input("Gib eine Zeichenkette ein, die in eine Zahl umgewandelt werden soll: ")
        umgewandelte_zahl = zeichenkette_in_zahl(zeichenkette)
        # f) Kontrollstruktur für umgewandelte Zahl
        if umgewandelte_zahl is not None:
            if umgewandelte_zahl > 0:
                print("Die Zahl ist positiv.")
            elif umgewandelte_zahl < 0:
                print("Die Zahl ist negativ.")
            else:
                print("Die Zahl ist Null.")
    elif aktion == 'beenden':
        break
    else:
        print("Ungültige Eingabe. Bitte versuche es erneut.")