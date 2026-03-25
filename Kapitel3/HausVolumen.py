#-------------------------------------------------
# Dateiname: HausVolumen
# Das Programm berechnet berechnet das Volumen 
# eines Hauses mit Satteldach
# Autor: Lena
# Letzte Änderung: 04.06.2025
#-------------------------------------------------
print('Volumenberechnung eines Hauses mit Satteldach')

# Eingabe   
laenge = float(input("Bitte geben Sie die Länge des Hauses in m ein: "))
breite = float(input("Bitte geben Sie die Breite des Hauses in m ein: "))   
hoehe = float(input("Bitte geben Sie die Höhe des Hauses in m ein: "))
dachhoehe = float(input("Bitte geben Sie die Höhe des Daches in m ein: "))

# Berechnung
volumen = laenge * breite * hoehe + (laenge * breite * dachhoehe) / 2

# Ausgabe
print(f'Das Volumen des Hauses beträgt {volumen:.2f} m³.')

# Ende des Programms