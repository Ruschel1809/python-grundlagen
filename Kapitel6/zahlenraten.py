#---------------------------------------------------------------
# Dateiname: zahlenraten.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm beinhaltet eine Funktion, die es dem Nutzer ermöglicht, eine Zahl zu raten mit so wenig Fragen wie möglich.
# Autor: Lena
# Letzte Änderung: 12.06.2025
#---------------------------------------------------------------
import random
def zahlen_raten() -> None:
    """
    Ein einfaches Zahlraten-Spiel, bei dem der Nutzer eine zufällig generierte Zahl zwischen 1 und 100 erraten muss.
    """
    zahl = random.randint(1, 100)
    versuche = 0
    gefunden = False

    print("Willkommen zum Zahlraten-Spiel!")
    print("Ich habe eine Zahl zwischen 1 und 100 gewählt. Versuche sie zu erraten!")

    while not gefunden:
        try:
            tipp = int(input("Gib deinen Tipp ein: "))
            versuche += 1
            
            if tipp < zahl:
                print("Zu niedrig! Versuch es nochmal.")
            elif tipp > zahl:
                print("Zu hoch! Versuch es nochmal.")
            else:
                gefunden = True
                print(f"Herzlichen Glückwunsch! Du hast die Zahl {zahl} in {versuche} Versuchen erraten.")
        except ValueError:
            print("Bitte gib eine gültige ganze Zahl ein.")

            