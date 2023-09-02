# Napisz funkcję, która z podanej listy zwróci wartość minimalną i maksymalną jednocześnie :)

nums = [3, 5, 1, 10, 6, 8]


def minmax(nums):
    return min(nums), max(nums)


minimum, maximum = minmax(nums)
print("Minimum:", minimum)
print("Maximum:", maximum)
