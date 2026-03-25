#---------------------------------------------------------------
# Dateiname: matheModul.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm verwendet unterschiedliche Funktionen und Konstanten aus math
# Autor: Lena
# Letzte Änderung: 12.06.2025
#---------------------------------------------------------------
import math as m

print(f"Wurzel aus 256 ist: {m.sqrt(256)}")

radius = 7
umfang = 2 * m.pi * radius
print(f"Der Umfang eines Kreises mit Radius {radius} ist: {umfang:.2f}")

def fahrenheit_zu_celsius(fahrenheit: float) -> float:
    """
    Konvertiert Fahrenheit in Celsius.
    
    :param fahrenheit: Temperatur in Fahrenheit
    :return: Temperatur in Celsius
    """
    return (fahrenheit - 32) * 5 / 9

print(f"68 Grad Fahrenheit sind {fahrenheit_zu_celsius(68):.2f} Grad Celsius.")

for i in range(1,6):
    print(i, end=' ')

# Import Funktion aus Modul:
# from modul time import sleep
# oder siehe oben ganzes Modul importieren 
