#---------------------------------------------------------------
# Dateiname: TemperaturUmrechner.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm wandelt Temperaturen zwischen Celsius und Fahrenheit um.
# Es erwartet die Eingaben temperatur und einheit vom Benutzer. einheit hat den Default C für Celsius.
# Autor: Lena
# Letzte Änderung: 11.06.2025
#---------------------------------------------------------------

def temperatur_umrechner(temperatur, einheit='C'):
    """
    Wandelt Temperaturen zwischen Celsius und Fahrenheit um.

    :param temperatur: Die Temperatur, die umgerechnet werden soll.
    :param einheit: Die Einheit der Temperatur ('C' für Celsius, 'F' für Fahrenheit). Standard ist 'C'.
    :return: Die umgerechnete Temperatur.
    """
    if einheit.upper() == 'C':
        # Umrechnung von Celsius nach Fahrenheit
        return (temperatur * 9/5) + 32
    elif einheit.upper() == 'F': 
        # Umrechnung von Fahrenheit nach Celsius
        return (temperatur - 32) * 5/9
    else:
        raise ValueError("Ungültige Einheit. Bitte 'C' für Celsius oder 'F' für Fahrenheit eingeben.")
    
weiter = True   
while weiter: 
    try:
        temperatur = float(input("Geben Sie die Temperatur ein: "))
        einheit = input("Geben Sie die Einheit ein (C für Celsius, F für Fahrenheit): ").strip().upper()
        umgerechnete_temperatur = temperatur_umrechner(temperatur, einheit)
        print(f"Die umgerechnete Temperatur ist: {umgerechnete_temperatur:.2f} {'F' if einheit == 'C' else 'C'}")
        if input("Möchten Sie eine weitere Umrechnung durchführen? (j/n): ").strip().lower() != 'j':
            weiter = False  
    except ValueError as e:
        if "could not convert string to float:" in e.args[0]:
            print("Bitte geben Sie eine gültige Zahl für die Temperatur ein.")
        elif "Ungültige Einheit" in e.args[0]:
            print("Bitte geben Sie 'C' für Celsius oder 'F' für Fahrenheit ein.")
        else:
            print(f"Fehler: {e}. Bitte versuchen Sie es erneut.")   
