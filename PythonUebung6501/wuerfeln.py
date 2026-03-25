#---------------------------------------------------------------
# Dateiname: wuerfeln.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm simuliert fünf Mal das Würfeln eines Würfels und gibt die Augenzahl aus.
# Autor: Lena
# Letzte Änderung: 13.06.2025
#---------------------------------------------------------------

import random as r, time as t

def wuerfeln() -> int:
    """Simuliert das Würfeln eines Würfels."""
    augenzahl = r.randint(1, 6)  # Zufällige Zahl zwischen 1 und 6
    return augenzahl

def aktuelle_timestamp() -> float:
    """Gibt die aktuelle Zeit als Timestamp zurück."""
    return t.time()


for i in range(5):  # Fünf Mal würfeln
    augenzahl = wuerfeln()  # Würfeln
    timestamp = aktuelle_timestamp()  # Aktuellen Timestamp abrufen
    print(f"Wurf {i + 1}: Augenzahl = {augenzahl}, Timestamp = {timestamp}")  # Ausgabe der Augenzahl und des Timestamps
    t.sleep(2)  # Zwei Sekunden warten, bevor der nächste Wurf erfolgt