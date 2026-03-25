#---------------------------------------------------------------
# Dateiname: randomModul.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm verwendet unterschiedliche Funktionen aus random
# Autor: Lena
# Letzte Änderung: 13.06.2025
#---------------------------------------------------------------

import math, random
zufallszahl = random.randint(1, 100)

def quadratwurzel(x: float) -> float:
    """
    Berechnet die Quadratwurzel einer Zahl.
    
    :param x: Die Zahl, von der die Quadratwurzel berechnet werden soll.
    :return: Die Quadratwurzel von x.
    """
    return math.sqrt(x)

if zufallszahl > 50:
    quadratwurzel(zufallszahl)
    print(f"Die Quadratwurzel von {zufallszahl} ist {quadratwurzel(zufallszahl):.2f}.")
else:
    print(f"Die Zufallszahl {zufallszahl} ist kleiner oder gleich 50, daher wird die Quadratwurzel nicht berechnet.")

for i in range(1,6):
    print(f"Die Quadratwqurzel von {i} ist {quadratwurzel(i):.2f}.")