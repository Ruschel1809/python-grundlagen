#---------------------------------------------------------------
# Dateiname: Datenanalyse.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm beinhaltet verschiedene Funktionen, um Produktdaten zu analysieren.
# Autor: Lena
# Letzte Änderung: 12.06.2025
#---------------------------------------------------------------

def durchschnitt(preise: list) -> float:
    """
    Berechnet den Durchschnitt einer Liste von Preisen.

    :param preise: Liste von Preisen
    :return: Durchschnitt der Preise in der Liste
    """
    if len(preise) == 0:
        return None  # Verhindert Division durch Null, wenn die Liste leer ist
    
    summe = 0.0
    for preis in preise:
        summe += preis
    
    return summe / len(preise)

def produkt_filter(produktnamen: list, filterstr: str) -> list:
    """
    Filtert die Produktnamen basierend auf einem Suchbegriff.

    :param produktnamen: Liste von Produktnamen
    :param filter: Suchbegriff zum Filtern der Produktnamen
    :return: Gefilterte Liste von Produktnamen
    """
    gefilterte_produkte = filter(lambda produkt: produkt.lower().startswith(filterstr.lower()), produktnamen)
    # Alternativ mit List Comprehension:
    # gefilterte_produkte = [produkt for produkt in produktnamen if filter.lower() in produkt.lower()]
    # Alternativ mit einer for-Schleife:
    # gefilterte_produkte = []
    # for produkt in produktnamen:
    #     if filter.lower() in produkt.lower():
    #         gefilterte_produkte.append(produkt)
    return gefilterte_produkte

def max_preis(produktpreise: list) -> float:
    """
    Findet rekursiv den maximalen Preis in einer Liste von Produktpreisen.

    :param produktpreise: Liste von Produktpreisen
    :return: Maximaler Preis in der Liste
    """
    if len(produktpreise) == 0:
        return None  # Verhindert Fehler bei leerer Liste
    if len(produktpreise) == 1:
        return produktpreise[0] 
    else:
        max_rest = max_preis(produktpreise[1:])
        maximaler_preis = produktpreise[0] if produktpreise[0] > max_rest else max_rest
    
    return maximaler_preis

def preis_mit_steuer(preis: float, steuersatz: float = 19) -> float:
    """
    Berechnet den Preis inklusive Steuern.

    :param preis: Integer Preis ohne Steuern
    :param steuersatz: Steuersatz in Prozent
    :return: Preis inklusive Steuern
    """
    neuer_preis = preis * (1 + steuersatz / 100)
    return neuer_preis

def erhoehe_preise(prozent_erhoehung : float, produkt_liste: list) -> list:
    """
    Erhöht die Preise in einer Liste um einen bestimmten Prozentsatz.

    :param prozent_erhoehung: Prozentsatz zur Erhöhung der Preise
    :return: Liste mit erhöhten Preisen
    """
    return list(map(lambda produkt: (produkt[0], produkt[1] * (1 + prozent_erhoehung / 100)), produkt_liste))

def drucke_produktliste(produkt_liste: list) -> None:
    """
    Druckt die Produktliste in einem lesbaren Format.

    :param produkt_liste: Liste von Produkten mit Preisen
    """
    for produkt, preis in produkt_liste:
        print(f"{produkt}: {preis:.2f} €")


produkt_liste = [("Laptop", 999.00), ("Smartphone", 599.00), ("Tablet", 399.00), ("Smartwatch", 499.00), ("Kopfhörer", 149.00), ("E-Book-Reader", 129.00), ("Fitness-Tracker", 79.00), ("Bloototh-Lautsprecher", 89.00), ("Powerbank", 39.00), ("Webcam", 59.00)]

preisliste = [produkt[1] for produkt in produkt_liste]
produktnamen = [produkt[0] for produkt in produkt_liste]

print(f"Durchschnittspreis: {durchschnitt(preisliste):.2f} €")
print(f"Gefilterte Produkte (enthält 'Smart'): {list(produkt_filter(produktnamen, 'Smart'))}")
print(f"Maximaler Preis: {max_preis(preisliste):.2f} €")
print(f"Preis inklusive Steuern (19%): {preis_mit_steuer(preisliste[0]):.2f} € für den Laptop")
print(f"Preise nach 10% Erhöhung:")
drucke_produktliste(erhoehe_preise(10, produkt_liste))