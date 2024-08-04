from city_function import city


def test_city():
    assert city("New York", "USA") == "New York, USA"
    assert city("London", "UK") == "London, UK"
    assert city("Paris", "France") == "Paris, France"
    assert city("Tokyo", "Japan") == "Tokyo, Japan"
    assert city("Berlin", "Germany") == "Berlin, Germany"
    assert city("Madrid", "Spain") == "Madrid, Spain"
