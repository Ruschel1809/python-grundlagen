#-------------------------------------------------------------
# Dateiname: Quiz.py
# Beschreibung:
# Das Programm stellt 3 Multiple-Choice-Fragen und wertet die Antworten aus. 
# Autor: Lena
# Letzte Änderung: 05.06.2025
#---------------------------------------------------------------

 antwort1 = input("Was ist die Hauptstadt von Deutschland?\nA) Berlin\nB) München\nC) Hamburg\nAntwort: ").strip().upper()
 if(antwort1 == "A"):
     print("Richtig!")
 else:
     while(antwort1 != "A"):
         print("Falsch! Versuche es noch einmal.")
         antwort1 = input("Was ist die Hauptstadt von Deutschland?\nA) Berlin\nB) München\nC) Hamburg\nAntwort: ").strip().upper()

 antwort2 = input("Welcher Planet ist der sonnennächste?\nA) Venus\nB) Mars\nC) Merkur\nAntwort: ").strip().upper()
 if(antwort2 == "C"):
     print("Richtig!")  
 else: 
     while(antwort2 != "C"):
         print("Falsch! Versuche es noch einmal.")
         antwort2 = input("Welcher Planet ist der sonnennächste?\nA) Venus\nB) Mars\nC) Merkur\nAntwort: ").strip().upper()
 antwort3 = input("Was ist die chemische Formel für Wasser?\nA) CO2\nB) H2O\nC) O2\nD) NaCl\nAntwort: ").strip().upper()
 if(antwort3 == "B"):
     print("Richtig!")
 else:
     while(antwort3 != "B"):
         print("Falsch! Versuche es noch einmal.")
         antwort3 = input("Was ist die chemische Formel für Wasser?\nA) CO2\nB) H2O\nC) O2\nAntwort: ").strip().upper()
 print("Herzlichen Glückwunsch! Du hast alle Fragen richtig beantwortet!")
