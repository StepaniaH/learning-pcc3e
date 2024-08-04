from pathlib import Path
import json

num = input("Enter your favorite number: ")
path = Path("favorite_number.json")
contents = json.dumps(str(num))
path.write_text(contents)
