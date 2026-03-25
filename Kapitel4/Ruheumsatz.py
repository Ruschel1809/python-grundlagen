#-------------------------------------------------------------
# Dateiname: Ruheumsatz.py
# Beschreibung:
# Das Programm berechnet den Grundumsatz eines 
# Menschen basierend auf Geschlecht, Alter, Größe und Gewicht. 
# Autor: Lena
# Letzte Änderung: 05.06.2025
#---------------------------------------------------------------
# Eingabe der Benutzerdaten
geschlecht = input("Bitte geben Sie Ihr Geschlecht ein (m/w): ").lower()
alter = int(input("Bitte geben Sie Ihr Alter in Jahren ein: "))
groesse = float(input("Bitte geben Sie Ihre Größe in cm ein: "))
gewicht = float(input("Bitte geben Sie Ihr Gewicht in kg ein: "))
# Berechnung des Grundumsatzes
if geschlecht == 'm':
    grundumsatz = 66.5 + (13 * gewicht) + (5 * groesse) - (6.8 * alter)
    print(f"Ihr Grundumsatz beträgt {grundumsatz:.2f} kcal pro Tag.")
elif geschlecht == 'w':
    grundumsatz = 655 + (9.6 * gewicht) + (1.8 * groesse) - (4.7 * alter)
    print(f"Ihr Grundumsatz beträgt {grundumsatz:.2f} kcal pro Tag.")
else:
    print("Ungültige Eingabe für Geschlecht. Bitte geben Sie 'm' für männlich oder 'w' für weiblich ein.")