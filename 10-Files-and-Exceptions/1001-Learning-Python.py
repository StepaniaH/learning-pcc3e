from pathlib import Path

print(Path("learning_python.txt").read_text())

print('\n')

for line in Path("learning_python.txt").read_text().splitlines():
    print(line)
