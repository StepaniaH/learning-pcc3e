favorite_places = {
    'Bob': ['New York', 'Chicago', 'Los Angeles'],
    'John': ['China', 'Japan', 'Korea'],
    'Tom': ['Tokyo', 'Osaka', 'Kyoto'],
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f" - {place}")
