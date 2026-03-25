#-------------------------------------------------
# Dateiname: Bremsweg
# Das Programm fragt nach der Geschwindigkeit und
# Bremswegverzögerung und berechnet den Bremsweg.
# Autor: Lena
# Letzte Änderung: 04.06.2025
#-------------------------------------------------

#Eingabe
print('Bremswegberechnung')
geschwindigkeit = float(input("Bitte geben Sie die Geschwindigkeit in m/s ein: "))
asphalt = input('Ist die Straße nass? (ja/nein): ').strip().lower()
if(asphalt == 'ja'):
    bremswegverzoegerung = 7
else:
    bremswegverzoegerung = 8
    
#Berechnung
bremsweg = (geschwindigkeit ** 2) / (2 * bremswegverzoegerung)

#Ausgabe	
print(f'Der Bremsweg beträgt {bremsweg:.2f} m.') # . gibt an, dass es Nachkommastellen hat, 2 dass 2 Nachkommastellen angezeigt werden sollen und f, dass es eine Fließkommazahl ist
# Ende des Programms