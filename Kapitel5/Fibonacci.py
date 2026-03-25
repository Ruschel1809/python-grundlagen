#---------------------------------------------------------------
# Dateiname: Fibonacci.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm berechnet die n-te Fibonacci-Zahl mittel einere rekursiven Funktion.
# Autor: Lena
# Letzte Änderung: 11.06.2025
#---------------------------------------------------------------

# def fibonacci(n):
#     """
#     Berechnet die n-te Fibonacci-Zahl.

#     :param n: Die Position in der Fibonacci-Folge (0-basierter Index).
#     :return: Die n-te Fibonacci-Zahl.
#     """
#     if n < 0:
#         raise ValueError("n muss eine nicht-negative ganze Zahl sein.")
#     elif n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         a, b = 0, 1
#         for _ in range(2, n + 1):
#             a, b = b, a + b
#         return b
    
def fibonacci(n):
    if n < 0:
        return print("n muss eine nicht-negative ganze Zahl sein.")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:    
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(7)) 