#---------------------------------------------------------------
# Dateiname: randUndMathModul.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm verwendet unterschiedliche Funktionen aus random und math
# Autor: Lena
# Letzte Änderung: 12.06.2025
#---------------------------------------------------------------

import math as m, random as r 

zufalls_zahl = r.randint(1, 10)

def berechne_quadrat(x: float) -> float:
    """
    Berechnet die Quadratwurzel einer Zahl.
    
    :param x: Die Zahl, von der die Quadratwurzel berechnet werden soll.
    :return: Die Quadratwurzel von x.
    """
    return x**2


if zufalls_zahl > 5:
    berechne_quadrat(zufalls_zahl)
    print(f"Das Quadrat von {zufalls_zahl} ist {berechne_quadrat(zufalls_zahl):.2f}.")
else:
    print(f"Die Zufallszahl {zufalls_zahl} ist kleiner oder gleich 5, daher wird das Quadrat nicht berechnet.")
for i in range(1,zufalls_zahl + 1):
    print(f"Die aktuelle Zahl ist {i}")