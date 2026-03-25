#---------------------------------------------------------------
# Dateiname: Entscheidungsbaum.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm hilft bei der Entscheidung ob man Sport treiben 
# soll, oder nicht, abhängig vom Wetter. 
# Autor: Lena
# Letzte Änderung: 05.06.2025
#---------------------------------------------------------------

# Eingabe der Wetterdaten
sonne = input("Scheint die Sonne? (ja/nein): ").lower()
regen = input("Regnet es? (ja/nein): ").lower()
wind= input("Ist es windig? (ja/nein): ").lower()
luftfeuchtigkeit = input("Ist die Luftfeuchtigkeit hoch? (ja/nein): ").lower()

# Entscheidungsbaum
if sonne == "ja":
    if(luftfeuchtigkeit == "ja"):
        print("Es ist sonnig und die Luftfeuchtigkeit ist hoch. Sport wäre nciht optimal, aber vielleicht ein ruhigen Spaziergang?")
    else:
        print("Es ist sonnig und die Luftfeuchtigkeit ist niedrig. Perfektes Wetter für Sport!")
else:
    if regen == "ja":
        print("Es ist sonnig, aber es regnet. Kein gutes Wetter für Sport, aber vielleicht ein Spaziergang im Regen?")
        if wind == "ja":
            print("Es ist sonnig und windig. Heute kein Sport, aber versuch es mit Drachen steigen lassen!")
        else:
            print("Es ist sonnig und ruhig. Sport frei!")
    else:
        print("Es ist bewölkt, aber kein Regen. Super Wetter für Sport!")