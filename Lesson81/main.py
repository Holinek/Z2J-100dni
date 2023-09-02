# Zadanie na dzisiaj:
# Napisz funkcję o nazwie compare_numbers(), która przyjmuje dwie liczby zmiennoprzecinkowe jako argumenty i porównuje
# je,uwzględniając potencjalne błędy zaokrąglenia. Funkcja powinna zwracać True, jeśli liczby są równe
# (z tolerancją błędu 1e-9), i False w przeciwnym razie.

def compare_numbers(a, b):
    epsilon = 1e-9
    return abs(a - b) < epsilon


a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
print(compare_numbers(a, b))
