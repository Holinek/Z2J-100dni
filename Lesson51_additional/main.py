# Zadanie dodatkowe:
# Policz tylko unikalne wyrazy.

text = input("Napisz jakieś zdanie, a ja policzę z ilu unikalnych wyrazów sie składa: ")
text = text.split()

for i in text:
    if text.count(i) > 1:
        while i in text:
            text.remove(i)
        else:
            continue

print("Ilość unikalnych wyrazów to:", len(text))
