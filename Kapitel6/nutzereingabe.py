#---------------------------------------------------------------
# Dateiname: nutzereingabe.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm importiert das Modul baumHoehe und nutzt die Funktion berechne_baumhoehe,
# um die Höhe eines Baums basierend auf der Nutzer-Eingabe zu berechnen.
# Autor: Lena
# Letzte Änderung: 12.06.2025
#---------------------------------------------------------------

import baumHoehe
def nutzereingabe() -> None:
    """
    Nimmt die Eingaben des Nutzers entgegen und berechnet die Höhe des Baums.
    """
    try:
        entfernung = float(input("Geben Sie die Entfernung zum Baum in Metern ein: "))
        augenhoehe = float(input("Geben Sie Ihre Augenhöhe in Metern ein: "))
        alpha = float(input("Geben Sie den Blickwinkel zur Spitze des Baums in Grad ein: "))
        
        hoehe = baumHoehe.berechne_baumhoehe(entfernung, augenhoehe, alpha)
        
        print(f"Die Höhe des Baums beträgt: {hoehe:.2f} Meter")
    except ValueError:
        print("Bitte geben Sie gültige numerische Werte ein.")

if __name__ == "__main__":
    nutzereingabe()