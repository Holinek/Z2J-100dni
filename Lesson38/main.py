# Zsumuj liczby parzyste (i oczywiście wydrukuj rezultat)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

a = 0

for i in numbers:
    if i % 2 == 0:
        a += i
print(a)
