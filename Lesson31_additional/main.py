# Zadanie ekstra dodatkowe:
# Napisz własną funkcję maximum(), która znajduje największą liczbę, nie używając gotowej komendy max().
# Masz już całą potrzebną do tego wiedzę.

numbers1 = [1, 3, 6, 12, 1, 23, 43, 12, 11]
numbers2 = [1, 3, 6, 12, 1, 23, 43, 12, 12]
numbers3 = [1, 3, 6, 12, 1, 23, 43, 12, 13]

numbers = [numbers1, numbers2, numbers3]


def print_maximum(value):
    print("Największa liczba to:", value)


def find_maximum(numbers_list):
    if not numbers_list:  # Handle an empty list
        return None

    biggest = numbers_list[0]  # Initialize with the first element

    for num in numbers_list:
        if biggest < num:
            biggest = num

    return biggest


for numbers_list in numbers:
    biggest = find_maximum(numbers_list)
    print_maximum(biggest)
