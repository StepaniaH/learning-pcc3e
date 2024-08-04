from pathlib import Path

Path("guest.txt").write_text(input("Plz enter your name: ").title())
