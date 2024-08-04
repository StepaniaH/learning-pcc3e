from pathlib import Path
import json

path = Path("favorite_number.json")
if path.exists():
    contents = path.read_text()
    num = json.loads(contents)
    print(f"I know your favorite number is {num}")
else:
    num = input("Enter your favorite number: ")
    contents = json.dumps(str(num))
    path.write_text(contents)
