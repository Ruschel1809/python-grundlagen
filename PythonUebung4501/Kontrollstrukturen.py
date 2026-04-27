#---------------------------------------------------------------
# Dateiname: DatenTypenKontrollstrukturen.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm wandelt eine eingegebene Zeichenkette in eine Ganzzahl um und prüft ob sie kleiner, größer oder gleich 10 ist
# Autor: Lena
# Letzte Änderung: 06.06.2025
#---------------------------------------------------------------
zahl = input("Bitte geben Sie eine Zahl ein: ")
try:
    zahl = int(zahl)  # Umwandlung der Eingabe in eine Ganzzahl
    if zahl < 10:
        print(f"Die Zahl {zahl} ist kleiner als 10.")
    elif zahl > 10:
        print(f"Die Zahl {zahl} ist größer als 10.")
    else:
        print(f"Die Zahl {zahl} ist gleich 10.")
except ValueError:
    print("Die Eingabe ist keine gültige Ganzzahl. Bitte geben Sie eine Zahl ein.")

print(str(list(range(1,zahl+1))))  # Ausgabe der Zahlen von 1 bis zur eingegebenen Zahl (inklusive)
