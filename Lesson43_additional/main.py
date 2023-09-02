# Dodaj możliwość przeliczania jednostek miar (długości i ciężaru).
import os


def measure_converter(measure1, measure2, value):
    conversion_factors = {
        'mm': {'cm': 0.1, 'dm': 0.01, 'm': 0.001, 'km': 0.000001, 'mm': 1},
        'cm': {'mm': 10, 'dm': 0.1, 'm': 0.01, 'km': 0.00001, 'cm': 1},
        'dm': {'mm': 100, 'cm': 10, 'm': 0.1, 'km': 0.0001, 'dm': 1},
        'm': {'mm': 1000, 'cm': 100, 'dm': 10, 'km': 0.001, 'm': 1},
        'km': {'mm': 1000000, 'cm': 100000, 'dm': 10000, 'm': 1000, 'km': 1},
        'g': {'dag': 0.1, 'kg': 0.001, 't': 0.000001, 'g': 1},
        'dag': {'g': 10, 'kg': 0.01, 't': 0.0001, 'dag': 1},
        'kg': {'g': 1000, 'dag': 100, 't': 0.001, 'kg': 1},
        't': {'g': 1000000, 'dag': 10000, 'kg': 1000, 't': 1}
    }

    if measure1 in conversion_factors and measure2 in conversion_factors[measure1]:
        conversion_factor = conversion_factors[measure1][measure2]
        return value * conversion_factor


def get_measure(prompt):
    while True:
        measure = input(prompt)
        measure = measure.lower()
        if measure in ["mm", "cm", "dm", "m", "km", "g", "dag", "kg", "t"]:
            return measure
        elif measure == "exit":
            return measure
        else:
            print("Błąd! Spróbuj ponownie :)")


def get_value():
    while True:
        try:
            value = input("Podaj warość, którą chcesz przeliczyć: ")
            return float(value)
        except ValueError:
            print("Błędna liczba")


def print_result(measure1, measure2, value, result):
    print("Wartość po przeliczeniu =", result, measure2)
    input("Wciśnij Enter, żeby kontynuować...")
    os.system('cls' if os.name == 'nt' else 'clear')


def run_converter():
    print("Podaj miarę długości/ciężaru z której chcesz przeliczyć wartość lub wpisz 'exit'")
    measure1 = get_measure("długość:[mm, cm, dm, m, km] | ciężar:[g, dag, kg, t] | wyjście:[exit]: ")
    if measure1 == "exit":
        return False
    print("Podaj miarę długości/ciężaru na którą chcesz przeliczyć wartość lub wpisz 'exit'")
    if measure1 in ["mm", "cm", "dm", "m", "km"]:
        measure2 = get_measure("długość:[mm, cm, dm, m, km] | wyjście:[exit]: ")
        if measure1 and measure2 in ["mm", "cm", "dm", "m", "km"]:
            value = get_value()
            result = measure_converter(measure1, measure2, value)
            print_result(measure1, measure2, value, result)
            return True
        elif measure2 == "exit":
            return False
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Błąd! Spróbuj ponownie :)")
            return True
    elif measure1 in ["g", "dag", "kg", "t"]:
        measure2 = get_measure("ciężar:[g, dag, kg, t] | wyjście:[exit]: ")
        if measure1 and measure2 in ["g", "dag", "kg", "t"]:
            value = get_value()
            result = measure_converter(measure1, measure2, value)
            print_result(measure1, measure2, value, result)
            return True
        elif measure2 == "exit":
            return False
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Błąd! Spróbuj ponownie :)")
            return True


def desc():
    print("Witaj w przeliczniku miar długości i ciężaru")
    print("Będziesz mógł przeliczyć długość: mm, cm, dm, m, km")
    print("Będziesz mógł przeliczyć ciężar: g, dag, kg, t")
    print("Jeśli chcesz zamknąć kalkulator wpisz 'exit'")
    print()


x = True
desc()
while x:
    x = run_converter()
