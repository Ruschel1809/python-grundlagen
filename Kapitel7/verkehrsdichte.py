#---------------------------------------------------------------
# Dateiname: verkehrsdichte.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm misst die Verkehrsdichte, in dem eine Minute lang
# Autos, Fahrräder und Personen gezählt werden
# Autor: Lena
# Letzte Änderung: 17.06.2025
#---------------------------------------------------------------

from time import time

print("Zähle den Verkehr und gib ein:\n""f: Fahrräder\n", "a: Autos\n", "p: Personen", sep='')
fahrraeder = 0
autos = 0
personen = 0
start_zeit=time()

while time() - start_zeit <= 60:
    eingabe=input("Auswahl: ")
    if eingabe == "f":
        fahrraeder += 1
    elif eingabe == "a":
        autos += 1
    elif eingabe == "p":
        personen += 1
    else:
        print("Ungültige Eingabe")
print("Verkährszählung nach einer Minute:\n", f"Fahrräder {fahrraeder}\nAutos {autos}\nPersonen {personen}", sep='' )