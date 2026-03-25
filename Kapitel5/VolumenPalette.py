#---------------------------------------------------------------
# Dateiname: VolumenPalette.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm berechnet das Volumen einer Palette. 
# Autor: Lena
# Letzte Änderung: 11.06.2025
#---------------------------------------------------------------

def volumen(l, b, d=2):
    """
    Berechnet das Volumen einer Palette.

    :param länge: Länge der Palette in Metern
    :param breite: Breite der Palette in Metern
    :param höhe: Höhe der Palette in Metern (Standardwert ist 2 Meter)
    :return: Volumen der Palette in Kubikmetern
    """
    return l * b * d
print(volumen(l=20,b=40))