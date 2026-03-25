#-------------------------------------------------
# Dateiname: ReisekostenAssistent
# Das Programm berechnet Kosten für eine 
# Gruppenreise mit einem Bus
# Autor: Lena
# Letzte Änderung: 04.06.2025
#-------------------------------------------------

print('Kostenplan für eine Gruppenreise')
# Eingabe
teilnehmer = int(input("Bitte geben Sie die Anzahl der Teilnehmer ein: "))
buskosten = float(input("Bitte geben Sie die Kosten für den Bus in € ein: "))
hotel = float(input("Bitte geben Sie die Kosten für das Hotel pro Person in € ein: "))
reisefuehrer = float(input("Bitte geben Sie die Kosten für den Reiseleiter in € ein: "))

# Berechnung
gesamt_kosten = buskosten + (hotel * teilnehmer) + reisefuehrer
if(teilnehmer > 0):
    kosten_pro_person = gesamt_kosten / teilnehmer
else:
    kosten_pro_person = 0   

# Ausgabe
print(f'Die Gesamtkosten der Reise betragen {gesamt_kosten:.2f} €.')
print(f'Die Kosten pro Person betragen {kosten_pro_person:.2f} €.')

# Ende des Programms