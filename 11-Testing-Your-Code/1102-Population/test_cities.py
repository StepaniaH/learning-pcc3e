from city_function import city_1, city_2


def test_city_1():
    assert city_1("New York", "USA",
                  100000000) == "New York, USA - population 100000000"
    assert city_1("London", "UK",
                  100000000) == "London, UK - population 100000000"
    assert city_1("Paris", "France",
                  100000000) == "Paris, France - population 100000000"
    assert city_1("Tokyo", "Japan",
                  100000000) == "Tokyo, Japan - population 100000000"
    assert city_1("Berlin", "Germany",
                  100000000) == "Berlin, Germany - population 100000000"
    assert city_1("Madrid", "Spain",
                  100000000) == "Madrid, Spain - population 100000000"


def test_city_2():
    assert city_2("New York", "USA") == "New York, USA - population "
    assert city_2("London", "UK") == "London, UK - population "
    assert city_2("Paris", "France") == "Paris, France - population "
    assert city_2("Tokyo", "Japan") == "Tokyo, Japan - population "
    assert city_2("Berlin", "Germany") == "Berlin, Germany - population "
    assert city_2("Madrid", "Spain") == "Madrid, Spain - population "
    assert city_2("New York", "USA",
                  100000000) == "New York, USA - population 100000000"
