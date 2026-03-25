#---------------------------------------------------------------
# Dateiname: lottozahlen.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm simuliert die Ziehung von Lottozahlen
# Autor: Lena
# Letzte Änderung: 17.06.2025
#---------------------------------------------------------------

from random import choice

def ziehe_element() -> int:
   return choice(range(1,50))

print("Ziehung der Lottozahlen")
for _ in range(6):
    print(ziehe_element(), end=" ")