favorite_numbers = {
    "John": [1, 2, 3],
    "Mary": [4, 5, 6],
    "Mike": [7, 8, 9],
    "Sarah": [10, 11, 12],
    "Tom": [13, 14, 15]
}

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f" - {number}")
