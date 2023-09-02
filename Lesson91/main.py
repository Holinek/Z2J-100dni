# Teraz czas na zadanie! Napisz funkcję divide(a, b), która dzieli dwie liczby.
# Funkcja powinna zgłaszać wyjątki w następujących sytuacjach:
# 1.Jeśli a lub b nie są liczbami, zgłoś TypeError.
# 2.Jeśli b wynosi 0, zgłoś ZeroDivisionError.
# 3.Jeśli a lub b są ujemne, zgłoś własny wyjątek NegativeNumberException.
# Następnie użyj bloku try...except, aby przechwycić i obsłuży każdy z tych wyjątków indywidualnie.

class NegativeNumberException(Exception):
    pass


def divide(a, b):
    try:
        if a < 0 or b < 0:
            raise NegativeNumberException("Podane liczby nie mogą być ujemne")
        return a / b
    except (TypeError, ZeroDivisionError, NegativeNumberException) as e:
        return f"Błąd: {e}"


print(divide(5, -5))
print(divide(5, 0))
print(divide(5, 2))
