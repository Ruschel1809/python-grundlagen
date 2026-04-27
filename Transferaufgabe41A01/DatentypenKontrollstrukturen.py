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
