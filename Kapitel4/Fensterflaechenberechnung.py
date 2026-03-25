#---------------------------------------------------------------
# Dateiname: Fensterflaechenberechnung.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm berechnet die gesamte Fensterfläche eines Hauses.
# Autor: Lena
# Letzte Änderung: 05.06.2025
#---------------------------------------------------------------

breite = float(input("Bitte geben Sie die Breite des Fensters in Metern ein: "))
hoehe = float(input("Bitte geben Sie die Höhe des Fensters in Metern ein: "))
anzahl = int(input("Bitte geben Sie die Anzahl der Fenster ein: "))

# Berechnung der Fensterfläche
fensterFlaeche = breite * hoehe * anzahl
print(f"Die gesamte Fensterfläche beträgt {fensterFlaeche:.2f} Quadratmeter.")

andereFenster = input("Gibt es Fenster mit anderen Maßen? (ja/nein): ").lower()

while andereFenster == "ja":
    breite = float(input("Bitte geben Sie die Breite des Fensters in Metern ein: "))
    hoehe = float(input("Bitte geben Sie die Höhe des Fensters in Metern ein: "))
    anzahl = int(input("Bitte geben Sie die Anzahl der Fenster ein: "))
    
    # Berechnung der Fensterfläche
    fensterFlaeche += breite * hoehe * anzahl
    print(f"Die gesamte Fensterfläche beträgt jetzt {fensterFlaeche:.2f} Quadratmeter.")
    
    andereFenster = input("Gibt es weitere Fenster mit anderen Maßen? (ja/nein): ").lower()

print("Auf Wiedersehen!")