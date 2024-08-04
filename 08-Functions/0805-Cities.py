def describe_city(name, country="USA"):
    print(f"{name.title()} is in {country.title()}")


describe_city("New York")
describe_city("Hong Kong", "China")
describe_city(country="Japan", name="Tokyo")
