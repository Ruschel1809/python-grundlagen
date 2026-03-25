#-------------------------------------------------------------
# Dateiname: Quiz.py
# Beschreibung:
# Das Programm stellt 3 Multiple-Choice-Fragen und wertet die Antworten aus. 
# Autor: Lena
# Letzte Änderung: 05.06.2025
#---------------------------------------------------------------

# antwort1 = input("Was ist die Hauptstadt von Deutschland?\nA) Berlin\nB) München\nC) Hamburg\nAntwort: ").strip().upper()
# if(antwort1 == "A"):
#     print("Richtig!")
# else:
#     while(antwort1 != "A"):
#         print("Falsch! Versuche es noch einmal.")
#         antwort1 = input("Was ist die Hauptstadt von Deutschland?\nA) Berlin\nB) München\nC) Hamburg\nAntwort: ").strip().upper()

# antwort2 = input("Welcher Planet ist der sonnennächste?\nA) Venus\nB) Mars\nC) Merkur\nAntwort: ").strip().upper()
# if(antwort2 == "C"):
#     print("Richtig!")  
# else: 
#     while(antwort2 != "C"):
#         print("Falsch! Versuche es noch einmal.")
#         antwort2 = input("Welcher Planet ist der sonnennächste?\nA) Venus\nB) Mars\nC) Merkur\nAntwort: ").strip().upper()
# antwort3 = input("Was ist die chemische Formel für Wasser?\nA) CO2\nB) H2O\nC) O2\nD) NaCl\nAntwort: ").strip().upper()
# if(antwort3 == "B"):
#     print("Richtig!")
# else:
#     while(antwort3 != "B"):
#         print("Falsch! Versuche es noch einmal.")
#         antwort3 = input("Was ist die chemische Formel für Wasser?\nA) CO2\nB) H2O\nC) O2\nAntwort: ").strip().upper()
# print("Herzlichen Glückwunsch! Du hast alle Fragen richtig beantwortet!")

#MUSTERLÖSUNG
# Initialisiere die Zählvariable für die richtigen Antworten

richtige_antworten = 0
# Frage 1

print("Frage 1: Was ist die Hauptstadt von Frankreich?")
print("a) Marseille\nb) Paris\nc) Lyon")
antwort = input("Deine Antwort (a, b, c): ")
while antwort not in ['a', 'b', 'c']:
    print("Ungültige Eingabe. Bitte wähle a, b, oder c.")
    antwort = input("Deine Antwort (a, b, c): ")
if antwort == 'b':
    richtige_antworten += 1
# Frage 2

print("Frage 2: Welcher Datentyp ist nicht veränderbar?")
print("a) Liste\nb) Tupel\nc) Wörterbuch")
antwort = input("Deine Antwort (a, b, c): ")
while antwort not in ['a', 'b', 'c']:
    print("Ungültige Eingabe. Bitte wähle a, b, oder c.")
    antwort = input("Deine Antwort (a, b, c): ")
if antwort == 'b':
    richtige_antworten += 1
# Frage 3

print("Frage 3: Welches Schlüsselwort wird in Python für eine unendliche Schleife verwendet?")
print("a) for\nb) while\nc) repeat")
antwort = input("Deine Antwort (a, b, c): ")
while antwort not in ['a', 'b', 'c']:
    print("Ungültige Eingabe. Bitte wähle a, b, oder c.")
    antwort = input("Deine Antwort (a, b, c): ")
if antwort == 'b':
    richtige_antworten += 1
# Gib die Anzahl der richtigen Antworten aus

print(f"Du hast {richtige_antworten} von 3 Fragen richtig beantwortet.")
# Rückmeldung basierend auf der Anzahl der richtigen Antworten

if richtige_antworten == 3:
    print("Ausgezeichnet! Du hast alle Fragen richtig beantwortet.")
elif richtige_antworten == 2:
    print("Gut gemacht! Du hast zwei Fragen richtig beantwortet.")
elif richtige_antworten == 1:
    print("Nicht schlecht! Du hast eine Frage richtig beantwortet.")
else:
    print("Schade! Vielleicht klappt es beim nächsten Mal besser.")