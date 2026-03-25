gz=[1,2,3,4,5] #zuweisung einer Liste mit Ganzzahlen auf die Variable gz
# Berechnung des Durchschnitts der Listenelemente
summe = sum(gz)  # Summe der Listenelemente
print("Die Summe der Listenelemente ist:", summe) # Ausgabe der Summe
if not gz:   # Überprüfung, ob die Liste leer ist
    print("Die Liste ist leer.")   # Ausgabe, wenn die Liste leer ist
else:
    durchschnitt = summe / len(gz)  # Durchschnitt berechnen
    print("Der Durchschnitt der Listenelemente ist:", durchschnitt)  # Ausgabe des Durchschnitts

eingabe = input("Bitte geben Sie eine Zahl ein: ").lower()  # Eingabeaufforderung für den Benutzer
if '.' in eingabe:  # Überprüfung, ob ein Punkt in der Eingabe enthalten ist
    print(f'Die Eingabe "{float(eingabe)}" ist eine Gleitkommazahl.')  # Ausgabe, wenn die Eingabe kein Integer ist
else:
    print(f'Die Eingabe "{int(eingabe)}" ist eine Ganzzahl.')  # Ausgabe, wenn die Eingabe ein Integer ist

evaEingabe1 = int(input("Bitte geben Sie eine Ganzzahl ein: "))  # Eingabeaufforderung für den Benutzer
evaEingabe2 = int(input("Bitte geben Sie eine weitere Ganzzahl ein: "))  # Eingabeaufforderung für den Benutzer
evaVerarbeitungMult = evaEingabe1 * evaEingabe2  # Multiplikation der beiden Ganzzahlen
# evaAusgabe
print(f"Das Ergebnis der Multiplikation von {evaEingabe1} und {evaEingabe2} ist: {evaVerarbeitungMult}")  # Ausgabe des Ergebnisses