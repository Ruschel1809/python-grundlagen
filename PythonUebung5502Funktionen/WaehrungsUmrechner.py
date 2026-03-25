#---------------------------------------------------------------
# Dateiname: TemperaturUmrechner.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm rechnet Währungen von Euro in US-Dollar oder Britischen Pfund um.
# Es erwartet die Eingaben betrag vom Benutzer. währung hat den Default 'USD' für US-Dollar.
# Autor: Lena
# Letzte Änderung: 11.06.2025
#---------------------------------------------------------------

def waehrungs_umrechner(betrag, waehrung='USD'):
    """
    Wandelt Beträge zwischen Euro und anderen Währungen um.

    :param betrag: Der Betrag in Euro, der umgerechnet werden soll.
    :param waehrung: Die Zielwährung ('USD' für US-Dollar, 'GBP' für Britische Pfund). Standard ist 'USD'.
    :return: Der umgerechnete Betrag.
    """
    if waehrung.upper() == 'USD':
        # Umrechnung von Euro nach US-Dollar
        return betrag * 1.1  # Beispielkurs
    elif waehrung.upper() == 'GBP':
        # Umrechnung von Euro nach Britischen Pfund
        return betrag * 0.9  # Beispielkurs
    else:
        raise ValueError("Ungültige Währung. Bitte 'USD' für US-Dollar oder 'GBP' für Britische Pfund eingeben.")
    
weiter = True
while weiter: 
    try:
        betrag = float(input("Geben Sie den Betrag in Euro ein: "))
        waehrung = input("Geben Sie die Währung ein (USD für US-Dollar, GBP für Britische Pfund): ").strip().upper()
        if '' == waehrung:
            umgerechneter_betrag = waehrungs_umrechner(betrag)
            waehrung = 'USD'
        else:       
            umgerechneter_betrag = waehrungs_umrechner(betrag, waehrung)
        print(f"Der umgerechnete Betrag ist: {umgerechneter_betrag:.2f} {waehrung}")
        if input("Möchten Sie eine weitere Umrechnung durchführen? (j/n): ").strip().lower() != 'j':
            weiter = False  
    except ValueError as e:
        if "could not convert string to float:" in e.args[0]:
            print("Bitte geben Sie einen gültigen Betrag ein.")
        elif "Ungültige Währung" in e.args[0]:
            print("Bitte geben Sie 'USD' für US-Dollar oder 'GBP' für Britische Pfund ein.")
        else:
            print(f"Fehler: {e}. Bitte versuchen Sie es erneut.")   

#---------------------------------------------------------------
# Musterlösung
# def umrechner(betrag, waehrung="USD"):
#     if waehrung == "USD":
#         return betrag * 1.1
#     elif waehrung == "GBP":
#         return betrag * 0.9
#     else:
#         return None
# while True:
#     print("Währungsumrechner: EUR zu USD oder GBP")
#     betrag = float(input("Bitte geben Sie den Betrag in EUR ein, den Sie umrechnen möchten: "))
#     waehrung = input("Bitte geben Sie die Währung ein, in die Sie umrechnen möchten (USD/GBP). Drücken Sie Enter für USD: ").upper()
    
#     if waehrung not in ["USD", "GBP", ""]:
#         print("Die angegebene Währung wird nicht unterstützt.")
#     else:
#         ergebnis = umrechner(betrag, waehrung)
#         if ergebnis is not None:
#             print(f"Umrechnungsergebnis: {ergebnis:.2f} {waehrung}")
#         else:
#             print("Es gab ein Problem mit der Währungsumrechnung.")
    
#     weiter = input("Möchten Sie eine weitere Umrechnung durchführen? (ja/nein): ").lower()
#     if weiter != "ja":
#         print("Programm beendet.")
#         break