# Twoim zadaniem jest stworzenie WŁASNEJ funkcji substring.
# Nie używaj systemowej, tylko napisz ją od zera (nie używaj slice(), ani [x:y])
# A jak już zaimplementujesz, wykonaj przy jej pomocy następujące zadania testowe -
# •	Z "Zero To Junior" wyciągnij 4 pierwsze znaki
# •	Z "Zero To Junior" wyciągnij 5 ostatnich znaków
# •	Znajdź w "Zero To Junior" ciąg "To" i pobierz wszystkie znaki od litery T do końca
# •	Wyciągnij z "Zero To Junior" znaki od 3 do 8

def substring(text, x, y):
    result = ""
    for i in range(x, y):
        result += text[i]
    return result


text = "Zero To Junior"

result1 = substring(text, 0, 4)
print(result1)

result2 = substring(text, len(text) - 5, len(text))
print(result2)

index = text.index("To")
result3 = substring(text, index, len(text))
print(result3)

result4 = substring(text, 3, 9)
print(result4)
