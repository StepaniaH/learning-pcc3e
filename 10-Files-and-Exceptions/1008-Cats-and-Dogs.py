from pathlib import Path

try:
    cats = Path("cats.txt")
    dogs = Path("dogs.txt")
    print(cats.read_text())
    print(dogs.read_text())
except FileNotFoundError:
    print("File not found.")
