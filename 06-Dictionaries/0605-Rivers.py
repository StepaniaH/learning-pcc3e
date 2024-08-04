rivers = {
    "Nile": "Egypt",
    "Ganges": "India",
    "Yangtze": "China"
}

for river, country in rivers.items():
    print(f"The {river} runs through {country}")

for river in rivers:
    print(f"{river}")

for country in rivers.values():
    print(f"{country}")
