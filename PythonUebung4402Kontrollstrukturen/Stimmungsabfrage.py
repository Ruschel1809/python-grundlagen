#---------------------------------------------------------------
# Dateiname: Stimmungsabfrage.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm fragt nach der Stimmung des Nutzer und reagiert 
# darauf, bis der Nutzer das Programm mit "nein" beendet.
# Autor: Lena
# Letzte Änderung: 06.06.2025
#---------------------------------------------------------------

while True: # Endlosschleife, um das Programm fortlaufend auszuführen
    stimmung = input("Wie ist deine aktuelle Stimmung? (glücklich/traurig/müde) ").lower() # Eingabeaufforderung für den Benutzer
    
    if stimmung == "glücklich": # Überprüfung der Stimmung
        print("Es ist toll zu hören, dass du glücklich bist!") # Ausgabe für glückliche Stimmung
    elif stimmung == "traurig": # Überprüfung der Stimmung
        print("Es tut mir leid zu hören, dass du traurig bist. Ich hoffe, es geht dir bald besser!") # Ausgabe für traurige Stimmung
    elif stimmung == "müde": # Überprüfung der Stimmung
        print("Vielleicht solltest du dich etwas ausruhen. Ruhe ist wichtig.") # Ausgabe für müde Stimmung
    else:
        print("Interessant! Ich weiß nicht viel über diese Stimmung.") # Ausgabe für unbekannte Eingabe
    
    beenden = input("Möchtest du das Programm beenden? (ja/nein) ").lower() # Abfrage, ob der Nutzer das Programm beenden möchte
    if beenden == "ja": # Wenn der Nutzer nein eingibt, wird die Schleife fortgesetzt, sonst beendet 
        print("Danke für Ihre Rückmeldung! Auf Wiedersehen!") 
        break # Ende der Schleife und des Programms


## # Dieses Skript fragt den Benutzer nach seiner Stimmung und gibt basierend darauf eine Antwort aus.

# Initialisiere eine Variable, um die Schleife zu steuern

# fortfahren = 'Nein'
# while fortfahren.lower() != 'ja':
#    # Schritt a: Eingabe der aktuellen Stimmung
#     stimmung = input("Wie ist deine aktuelle Stimmung? (glücklich, traurig, müde): ")
#    # Schritt b: Überprüfung der Eingabe und Ausgabe einer entsprechenden Nachricht

#     if stimmung == 'glücklich':
#         print("Es ist toll zu hören, dass du glücklich bist!")
#     elif stimmung == 'traurig':
#         print("Es tut mir leid zu hören, dass du traurig bist. Ich hoffe, es geht dir bald besser!")
#     elif stimmung == 'müde':
#         print("Vielleicht solltest du dich etwas ausruhen. Ruhe ist wichtig.")
#     else:
#         print("Interessant! Ich weiß nicht viel über diese Stimmung.")
#    # Schritt d: Abfrage, ob das Programm beendet werden soll

#     fortfahren = input("Möchtest du das Programm beenden? (Ja/Nein): ")