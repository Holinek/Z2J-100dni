# Zadanie na dzisiaj:
# Napisz funkcję, która przyjmuje listę liczb całkowitych i zwraca listę zawierającą tylko unikalne wartości z tej listy
# I teraz dwie podpowiedzi.
# •	Konwersja listy na set
# my_set = set(my_list)
# •	Konwersja set na listę
# my_list = list(my_set)

my_list = [1, 2, 3, 1, 2, 6, 3, 6, 7, 8, 9, 9, 7, 6, 4, 8]


def get_unique(my_list):
    return list(set(my_list))


print(get_unique(my_list))
