def schickeAusgabe(x):
   typ=str(type(x))
   if typ == "<class 'int'>":
       print('Der Datentyp von ' + str(x) + ' ist: int')
   elif typ == "<class 'float'>":
       print('Der Datentyp von ' + str(x) + ' ist: float')
   elif typ == "<class 'complex'>":
       print('Der Datentyp von ' + str(x) + ' ist: complex')
   elif typ == "<class 'str'>":
       print('Der Datentyp von ' + str(x) + ' ist: str')
   elif typ == "<class 'tuple'>":
       print('Der Datentyp von ' + str(x) + ' ist: tuple')
   elif typ == "<class 'list'>":
       print('Der Datentyp von ' + str(x) + ' ist: list')
   elif typ == "<class 'set'>":
       print('Der Datentyp von ' + str(x) + ' ist: set')
   else:
       print('Der Datentyp von ' + str(x) + ' ist: unbekannt')
   
i=42
f=2.0
c=3+4j
s='string'
t=('e',5)
l=[6,7,8]
set={'a','n'}
schickeAusgabe(i)
schickeAusgabe(f)
schickeAusgabe(c)
schickeAusgabe(s)
schickeAusgabe(t)
schickeAusgabe(l)
schickeAusgabe(set)
print(int(f)) # ein neues Objekt vom Typ int wird angelegt und der ganzzahligfe Wert der float Variable f wird zugewiesen
print(f"Der Datentyp von ganze_zahl ist: {type(i)}")
newList=[l[0], l[1], t[-1]]  # t[-1] greift auf das letzte Element des Tupels zu
print(newList)