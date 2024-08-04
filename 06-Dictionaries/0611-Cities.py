cities = {
    "Tokyo": {
        "country": "Japan",
        "population": 13929286,
        "fact": "The Tokyo Tower was built in 1959."
    },
    "New York": {
        "country": "USA",
        "population": 8525137,
        "fact": "The Empire State Building was built in 1931."
    },
    "London": {
        "country": "UK",
        "population": 8908524,
        "fact": "The London Eye was built in 1889."
    },
}

for city in cities:
    for key, value in cities[city].items():
        print(f"{city.title()} {key.title()}: {value}")
    print("\n")
