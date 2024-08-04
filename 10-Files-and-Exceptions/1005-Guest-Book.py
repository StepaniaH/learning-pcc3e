from pathlib import Path

names = ""
while True:
    name = input(
        "You can enter 'quit' to quit the program. \nEnter a name: ").strip()
    if name.lower() == "quit":
        break

    names += name.title() + "\n"


Path("guest_book.txt").write_text(names)
