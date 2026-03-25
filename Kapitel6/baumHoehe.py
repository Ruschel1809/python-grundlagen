#---------------------------------------------------------------
# Dateiname: baumHoehe.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm berechnet die Höhe eines Baums. Der Nutzer gibt dafür die Werte: 
# Entfernung zum Baum, Augenhöhe und Blickwinkel alpha zur Spitze des Baums
# Autor: Lena
# Letzte Änderung: 12.06.2025
#---------------------------------------------------------------

import math
def berechne_baumhoehe(entfernung: float, augenhoehe: float, alpha: float) -> float:
    """
    Berechnet die Höhe eines Baums basierend auf der Entfernung, Augenhöhe und dem Blickwinkel.

    :param entfernung: Entfernung zum Baum in Metern
    :param augenhoehe: Augenhöhe des Betrachters in Metern
    :param alpha: Blickwinkel zur Spitze des Baums in Grad
    :return: Höhe des Baums in Metern
    """
    # Umwandlung des Blickwinkels von Grad in Bogenmaß
    alpha_rad = math.radians(alpha)
    
    # Berechnung der Baumhöhe
    baumhoehe = entfernung * math.tan(alpha_rad) + augenhoehe
    
    return baumhoehe

if __name__ == "__main__":
    # Beispielwerte
    entfernung = 10.0  # Entfernung zum Baum in Metern
    augenhoehe = 1.5   # Augenhöhe in Metern
    alpha = 30.0       # Blickwinkel in Grad
    
    # Berechnung der Baumhöhe
    hoehe = berechne_baumhoehe(entfernung, augenhoehe, alpha)
    
    print(f"Die Höhe des Baums beträgt: {hoehe:.2f} Meter")