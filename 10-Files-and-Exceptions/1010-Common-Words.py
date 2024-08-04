from pathlib import Path

try:
    path = Path("a.txt")
    words = path.read_text().lower()
except FileNotFoundError:
    pass
else:
    print(words.count("row"))
    print(words.count("the"))
    print(words.count("the "))


# I use (this article)[https://www.gutenberg.org/ebooks/73956].
