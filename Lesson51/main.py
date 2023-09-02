# Napisz aplikację, która:
# •	pobierze wiele linii, wpisanego na ekranie tekstu
# •	policzy wszystkie wyrazy i wypisze ich ilość na ekranie

text = input("Napisz jakieś zdanie, a ja policzę z ilu wyrazów sie składa: ")
text = text.split()

print("Ilość wyrazów to:", len(text))
