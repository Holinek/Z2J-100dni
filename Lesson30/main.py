# Zadanie na dzisiaj:
# Napisz funkcję printavg(value), która wydrukuje komunikat: "Średnia wynosi: ",a następnie wyświetli wyliczoną wartość.
def printavg(value):
    total = sum(value)
    count = len(value)
    avg = total / count
    print("Średnia wynosi: ", avg)


value1 = [1, 3, 6, 12, 1, 23, 43, 12, 11]
value2 = [1, 3, 6, 12, 1, 23, 43, 12, 12]
value3 = [1, 3, 6, 12, 1, 23, 43, 12, 13]

printavg(value1)
printavg(value2)
printavg(value3)
