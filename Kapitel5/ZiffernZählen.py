#---------------------------------------------------------------
# Dateiname: ZiffernZählen.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm erkennt die Ziffern in einem String und zählt ihr vorkommen. 
# Autor: Lena
# Letzte Änderung: 11.06.2025
#---------------------------------------------------------------

def ziffern(text):
    """
    Zählt die Vorkommen jeder Ziffer (0-9) in einem gegebenen Text.

    :param text: Der Eingabetext, in dem die Ziffern gezählt werden sollen.
    :return: Summe der Ziffern im Text.
    """
    ziffern = 0
    
    for zeichen in text:
        if zeichen.isdigit():
            ziffern += 1
            
    return ziffern
print(ziffern("Python 3"))